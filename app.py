import oracledb
from flask import Flask, jsonify
import sys

# 数据库配置
ORACLE_USER = "s2835812"
ORACLE_PASSWORD = "252525"
ORACLE_DSN = "172.16.108.21:1842/GLRNLIVE_PRMY.is.ed.ac.uk"

app = Flask(__name__)

def fetch_graveyards():
    conn = None
    try:
        conn = oracledb.connect(
            user=ORACLE_USER,
            password=ORACLE_PASSWORD,
            dsn=ORACLE_DSN,
        )
        cur = conn.cursor()
        
        cur.execute(
            """
            SELECT 
                name, latitude, longitude, area_hectares, 
                ndvi_mean, carbon_total_tonnes, carbon_per_hectare, 
                edi_norm, simd_rank, simd_decile
            FROM graveyards
            """
        )
        
        # 将查询结果转为字典
        columns = [col[0].lower() for col in cur.description]
        cur.rowfactory = lambda *args: dict(zip(columns, args))
        
        rows = cur.fetchall()
        
        # 格式化 JSON 结构
        formatted_rows = []
        for row in rows:
            formatted_rows.append({
                "id": row.get('name'),
                "name": row.get('name'),
                "latitude": row.get('latitude'),
                "longitude": row.get('longitude'),
                "areaHectares": row.get('area_hectares'),
                "ndvi": {"meanNdvi": row.get('ndvi_mean')},
                "carbon": {
                    "totalCarbonTonnes": row.get('carbon_total_tonnes'),
                    "carbonPerHectare": row.get('carbon_per_hectare')
                },
                "deprivation": {
                    "ediScore": row.get('edi_norm'),
                    "simdRank": row.get('simd_rank'),
                    "simdQuintile": row.get('simd_decile')
                }
            })
            
        return formatted_rows
        
    except Exception as e:
        # 在 gunicorn 错误日志里打印
        print(f"Database Error: {e}", file=sys.stderr)
        return {"error": str(e)}
    finally:
        if conn:
            conn.close()

@app.route("/")
def index():
    return "Group 1 Project API is Running!"

@app.route("/api/graveyards")
def api_graveyards():
    return jsonify(fetch_graveyards())

# 注意：这里不需要 app.run()，gunicorn 会直接调用 app 对象