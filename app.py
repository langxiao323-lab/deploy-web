import oracledb
import json
import os
import sys
from flask import Flask, jsonify, render_template

# --- 数据库配置 ---
ORACLE_USER = "s2835812"
ORACLE_PASSWORD = "252525"
ORACLE_DSN = "172.16.108.21:1842/GLRNLIVE_PRMY.is.ed.ac.uk"

app = Flask(__name__)

# --- 报告中的定性数据 (手动映射) ---
# 基于报告 Table 2.1.10 和 Text
REPORT_TAGS = {
    "Grange Cemetery": ["Biodiversity Hotspot", "334+ Species", "Heritage"],
    "Greyfriars Kirkyard": ["Tourist Attraction", "Harry Potter Connection", "Monument"],
    "Warriston Cemetery": ["High Canopy", "Biodiversity"],
    "Buccleuch": ["Priority Zone", "High Social Deprivation"],
    "Craigmillar Castle Park Cemetery": ["Priority Zone", "Low Carbon", "Social Hotspot"],
    "Dalry Cemetery": ["Community Garden", "High Density"],
    "Newington Cemetery": ["Highest EDI Score", "Dense Canopy"]
}

def determine_strata(carbon):
    if carbon is None: return "Unknown"
    val = float(carbon)
    if val > 100: return "High"
    if val > 50: return "Medium"
    return "Low"

def fetch_enriched_data():
    conn = None
    try:
        # 1. 读取 GeoJSON
        json_path = os.path.join(os.path.dirname(__file__), 'data', 'Cemeteries_35.json')
        if not os.path.exists(json_path):
            return {"features": []}

        with open(json_path, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)

        # 2. 数据库查询 (增加了 EDI 和 SIMD 字段)
        conn = oracledb.connect(
            user=ORACLE_USER,
            password=ORACLE_PASSWORD,
            dsn=ORACLE_DSN,
        )
        cur = conn.cursor()
        # 假设数据库里有 edi_norm 和 simd_decile 字段
        # 如果报错提示字段不存在，请检查你的数据库表结构
        cur.execute("""
            SELECT name, area_hectares, ndvi_mean, carbon_total_tonnes, 
                   edi_norm, simd_decile 
            FROM graveyards
        """)
        
        db_data = {}
        for row in cur:
            name = row[0]
            if name:
                db_data[name.strip()] = {
                    "area": row[1],
                    "ndvi": row[2],
                    "carbon": row[3],
                    "edi": row[4],      # 环境剥夺指数 (0-1)
                    "simd": row[5]      # 社会剥夺 (1-10, 1是最穷)
                }

        # 3. 数据融合
        for feature in geojson_data['features']:
            props = feature['properties']
            site_name = props.get('name', '').strip()
            
            # 注入数据库数据
            matched = db_data.get(site_name)
            if matched:
                c_val = matched['carbon'] or 0
                props.update({
                    "Strata": determine_strata(c_val),
                    "Area": (matched['area'] or 0) * 10000,
                    "Carbon": c_val,
                    "Canopy": (matched['ndvi'] or 0) * 100,
                    "EDI": matched['edi'] or 0,
                    "SIMD": matched['simd'] or 0, # SIMD Decile
                    "has_data": True
                })
            else:
                props.update({
                    "Strata": "Unknown", "Carbon": 0, "EDI": 0, "SIMD": 0, "has_data": False
                })

            # 注入报告标签
            props['ReportTags'] = REPORT_TAGS.get(site_name, [])

        return geojson_data

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return {"features": []}
    finally:
        if conn: conn.close()

# --- 路由 ---
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
    app.run(host='0.0.0.0', port=55429, debug=True)