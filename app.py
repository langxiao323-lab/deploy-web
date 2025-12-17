import oracledb
import json
import os
import sys
import getpass
from flask import Flask, jsonify, render_template, send_from_directory

# --- Oracle Database Configuration ---
print("=== Oracle Database Login ===")
ORACLE_USER = input("Username: ")
ORACLE_PASSWORD = getpass.getpass("Password: ")
ORACLE_DSN = "172.16.108.21:1842/GLRNLIVE_PRMY.is.ed.ac.uk"
print("Credentials set successfully!\n")

app = Flask(__name__, template_folder='web')

# --- Name Mapping (GeoJSON name -> Database name) ---
# Based on actual database names from 02_insert_data.sql
NAME_MAPPING = {
    "Liberton Churchyard": "Liberton Cemetery",
    "St Mary's Ratho": "St Mary's Ratho",  # Apostrophe match
    # Note: The following GeoJSON names have no database entries:
    # - Mount Vernon Cemetery (closest by area: no unique match)
    # - Colinton Cemetery (southern section)
    # - Colinton Cemetery (northern section)
}

# --- Report Tags (from Report Table 2.1.10) ---
REPORT_TAGS = {
    "Grange Cemetery": ["Biodiversity Hotspot", "334+ Species", "Heritage"],
    "Greyfriars Kirkyard": ["Tourist Attraction", "Harry Potter Connection", "Monument"],
    "Warriston Cemetery": ["High Canopy", "Biodiversity"],
    "Buccleuch": ["Priority Zone", "High Social Deprivation"],
    "Craigmillar Castle Park Cemetery": ["Priority Zone", "Low Carbon", "Social Hotspot"],
    "Dalry Cemetery": ["Community Garden", "High Density"],
    "Newington Cemetery": ["Highest EDI Score", "Dense Canopy"]
}

def fetch_enriched_data():
    conn = None
    try:
        # 1. Read GeoJSON file
        json_path = os.path.join(os.path.dirname(__file__), 'data', 'Cemeteries_35.json')
        if not os.path.exists(json_path):
            print(f"ERROR: GeoJSON file not found at {json_path}", file=sys.stderr)
            return {"features": []}

        with open(json_path, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)
        
        print(f"Loaded GeoJSON with {len(geojson_data.get('features', []))} features", file=sys.stderr)

        # 2. Connect to Oracle database and fetch data
        print("Connecting to Oracle database...", file=sys.stderr)
        conn = oracledb.connect(
            user=ORACLE_USER,
            password=ORACLE_PASSWORD,
            dsn=ORACLE_DSN,
        )
        cur = conn.cursor()
        
        # Query total carbon from database (calculated from corrected data)
        cur.execute("""
            SELECT SUM(carbon_per_hectare_calibrate * area_m2 / 10000) FROM graveyards
        """)
        total_carbon_db = cur.fetchone()[0] or 0
        
        # Query database - get all required fields (calculate total carbon from corrected data)
        cur.execute("""
            SELECT name, strata, area_m2, ndvi_mean, 
                   carbon_per_hectare_calibrate, edi_norm, simd_decile, 
                   canopy_percentage, 
                   (carbon_per_hectare_calibrate * area_m2 / 10000) AS calculated_carbon_total
            FROM graveyards
            ORDER BY name
        """)
        
        db_data = {}
        for row in cur:
            name = row[0]
            if name:
                # EDI normalized 0-1 scale (0=most deprived, 1=least deprived)
                edi_value = row[5] or 0
                
                db_data[name.strip()] = {
                    'Strata': row[1] or 'Unknown',
                    'Area': row[2] or 0,  # area_m2 directly
                    'NDVI': row[3] or 0,  # NDVI Mean
                    'CarbonPerHectare': row[4] or 0,  # carbon_per_hectare_calibrate
                    'EDI': edi_value,  # EDI normalized 0-1 scale
                    'SIMD': row[6] or 0,  # SIMD Decile
                    'Canopy': row[7] or 0,  # Canopy Percentage
                    'AGBTotal': row[8] or 0  # calculated: carbon_per_hectare_calibrate * area_m2 / 10000
                }
        
        print(f"Loaded {len(db_data)} cemeteries from database", file=sys.stderr)
        print(f"Database cemetery names: {list(db_data.keys())[:5]}...", file=sys.stderr)

        # Helper function to calculate polygon area from coordinates
        def calc_polygon_area(coords):
            n = len(coords)
            area = 0
            for i in range(n):
                j = (i + 1) % n
                area += coords[i][0] * coords[j][1]
                area -= coords[j][0] * coords[i][1]
            # Rough conversion to m2 (lat/lon to meters)
            return abs(area) / 2 * 111319.5 * 111319.5 * 0.7

        # 3. Merge database data with GeoJSON
        matched_count = 0
        unmatched_features = []
        used_db_names = set()
        
        # First pass: match by name
        for feature in geojson_data['features']:
            props = feature['properties']
            site_name = props.get('name', '').strip()
            
            # Match database data (try direct match first, then use mapping)
            db_name = NAME_MAPPING.get(site_name, site_name)
            matched = db_data.get(db_name)
            if matched:
                used_db_names.add(db_name)
                matched_count += 1
                props.update({
                    "Strata": matched['Strata'],
                    "Area": matched['Area'],
                    "CarbonPerHectare": matched['CarbonPerHectare'],
                    "AGBTotal": matched['AGBTotal'],
                    "Canopy": matched['Canopy'],
                    "EDI": matched['EDI'],
                    "SIMD": matched['SIMD'],
                    "NDVI": matched['NDVI'],
                    "has_data": True
                })
            else:
                unmatched_features.append(feature)

            # Inject report tags
            props['ReportTags'] = REPORT_TAGS.get(site_name, [])
        
        # Second pass: match unmatched features by area
        if unmatched_features:
            # Get unused db entries
            unused_db = {k: v for k, v in db_data.items() if k not in used_db_names}
            
            for feature in unmatched_features:
                props = feature['properties']
                site_name = props.get('name', '').strip()
                
                # Calculate GeoJSON polygon area
                try:
                    coords = feature['geometry']['coordinates'][0]
                    geo_area = calc_polygon_area(coords)
                except:
                    geo_area = 0
                
                # Find closest area match in unused db entries
                best_match = None
                best_diff = float('inf')
                for db_name, db_info in unused_db.items():
                    diff = abs(db_info['Area'] - geo_area)
                    if diff < best_diff:
                        best_diff = diff
                        best_match = (db_name, db_info)
                
                if best_match:
                    db_name, matched = best_match
                    used_db_names.add(db_name)
                    del unused_db[db_name]
                    matched_count += 1
                    print(f"Area matched: {site_name} ({geo_area:.0f}m2) -> {db_name} ({matched['Area']:.0f}m2)", file=sys.stderr)
                    props.update({
                        "Strata": matched['Strata'],
                        "Area": matched['Area'],
                        "CarbonPerHectare": matched['CarbonPerHectare'],
                        "AGBTotal": matched['AGBTotal'],
                        "Canopy": matched['Canopy'],
                        "EDI": matched['EDI'],
                        "SIMD": matched['SIMD'],
                        "NDVI": matched['NDVI'],
                        "has_data": True
                    })
                else:
                    props.update({
                        "Strata": "Unknown", 
                        "CarbonPerHectare": 0,
                        "AGBTotal": 0,
                        "EDI": 0, 
                        "SIMD": 0,
                        "NDVI": 0,
                        "Canopy": 0,
                        "has_data": False
                    })
        
        print(f"Successfully matched {matched_count} out of {len(geojson_data['features'])} features", file=sys.stderr)
        
        if matched_count == 0:
            print(f"WARNING: No matches found!", file=sys.stderr)
            print(f"Sample GeoJSON names: {[f['properties'].get('name') for f in geojson_data['features'][:3]]}", file=sys.stderr)
            print(f"Sample DB names: {list(db_data.keys())[:3]}", file=sys.stderr)
        elif unmatched_features:
            print(f"Unmatched names: {[f['properties'].get('name') for f in unmatched_features[:5]]}", file=sys.stderr)

        # Add total carbon from database to response
        geojson_data['totalCarbonFromDB'] = round(total_carbon_db, 1)
        
        return geojson_data

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return {"features": []}
    finally:
        if conn:
            conn.close()
            print("Database connection closed", file=sys.stderr)

# --- Routes ---
@app.route("/")
@app.route("/group1project")
@app.route("/group1project/")
@app.route("/dev/group1project")
@app.route("/dev/group1project/")
@app.route("/~s2835812/group1project")
@app.route("/~s2835812/group1project/")
def index():
    return render_template("map.html")

@app.route("/api/graveyards")
@app.route("/group1project/api/graveyards")
@app.route("/dev/group1project/api/graveyards")
@app.route("/~s2835812/group1project/api/graveyards")
def api_graveyards():
    return jsonify(fetch_enriched_data())

@app.route("/api/simd")
@app.route("/group1project/api/simd")
@app.route("/dev/group1project/api/simd")
@app.route("/~s2835812/group1project/api/simd")
def api_simd():
    simd_path = os.path.join(os.path.dirname(__file__), 'data', 'edinburgh_simd.json')
    try:
        with open(simd_path, 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    except Exception as e:
        print(f"Error loading SIMD data: {e}", file=sys.stderr)
        return jsonify({"features": []})

# Static files route for report images
@app.route("/dev/group1project/static/<path:filename>")
@app.route("/group1project/static/<path:filename>")
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    print(f"Starting Flask server on port 55429...", file=sys.stderr)
    print(f"Database: {ORACLE_DSN}", file=sys.stderr)
    app.run(host='0.0.0.0', port=55429, debug=True)