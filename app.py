import oracledb
import json
import os
import sys
from flask import Flask, jsonify, render_template

# --- Oracle Database Configuration ---
ORACLE_USER = "s2835812"
ORACLE_PASSWORD = "252525"
ORACLE_DSN = "172.16.108.21:1842/GLRNLIVE_PRMY.is.ed.ac.uk"

app = Flask(__name__)

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
        
        # Query database - get all required fields
        cur.execute("""
            SELECT name, strata, area_hectares, ndvi_mean, 
                   carbon_per_hectare_validate, edi_new_canopy_ndvi, simd_decile, 
                   canopy_percentage, agb_total
            FROM graveyards
            ORDER BY name
        """)
        
        db_data = {}
        for row in cur:
            name = row[0]
            if name:
                # Keep EDI in 0-100 range (do NOT divide by 100)
                edi_value = row[5] or 0
                
                db_data[name.strip()] = {
                    'Strata': row[1] or 'Unknown',
                    'Area': (row[2] or 0) * 10000,  # Convert hectares to m2
                    'NDVI': row[3] or 0,  # NDVI Mean
                    'CarbonPerHectare': row[4] or 0,  # carbon_per_hectare_validate
                    'EDI': edi_value,  # EDI new (Canopy % x NDVI) - keep 0-100 range
                    'SIMD': row[6] or 0,  # SIMD Decile
                    'Canopy': row[7] or 0,  # Canopy Percentage
                    'AGBTotal': row[8] or 0  # AGB Total
                }
        
        print(f"Loaded {len(db_data)} cemeteries from database", file=sys.stderr)
        print(f"Database cemetery names: {list(db_data.keys())[:5]}...", file=sys.stderr)

        # 3. Merge database data with GeoJSON
        matched_count = 0
        unmatched_names = []
        
        for feature in geojson_data['features']:
            props = feature['properties']
            site_name = props.get('name', '').strip()
            
            # Match database data
            matched = db_data.get(site_name)
            if matched:
                matched_count += 1
                props.update({
                    "Strata": matched['Strata'],
                    "Area": matched['Area'],
                    "CarbonPerHectare": matched['CarbonPerHectare'],
                    "AGBTotal": matched['AGBTotal'],
                    "Canopy": matched['Canopy'],
                    "EDI": matched['EDI'],  # 0-100 range
                    "SIMD": matched['SIMD'],
                    "NDVI": matched['NDVI'],
                    "has_data": True
                })
            else:
                unmatched_names.append(site_name)
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

            # Inject report tags
            props['ReportTags'] = REPORT_TAGS.get(site_name, [])
        
        print(f"Successfully matched {matched_count} out of {len(geojson_data['features'])} features", file=sys.stderr)
        
        if matched_count == 0:
            print(f"WARNING: No matches found!", file=sys.stderr)
            print(f"Sample GeoJSON names: {[f['properties'].get('name') for f in geojson_data['features'][:3]]}", file=sys.stderr)
            print(f"Sample DB names: {list(db_data.keys())[:3]}", file=sys.stderr)
        elif unmatched_names:
            print(f"Unmatched names: {unmatched_names[:5]}", file=sys.stderr)

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

if __name__ == "__main__":
    print(f"Starting Flask server on port 55429...", file=sys.stderr)
    print(f"Database: {ORACLE_DSN}", file=sys.stderr)
    app.run(host='0.0.0.0', port=55429, debug=True)