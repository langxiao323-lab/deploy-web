import oracledb
from flask import Flask, jsonify

ORACLE_USER = "s2835812"
ORACLE_PASSWORD = "252525"
ORACLE_DSN = "oracle.geos.ed.ac.uk:1521/ORCL"

app = Flask(__name__)

def fetch_graveyards():
    conn = oracledb.connect(
        user=ORACLE_USER,
        password=ORACLE_PASSWORD,
        dsn=ORACLE_DSN,
    )
    try:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT 
                id,
                name,
                latitude,
                longitude,
                area_hectares,
                ndvi_mean,
                carbon_total_tonnes,
                carbon_per_hectare,
                edi_norm,
                simd_rank,
                simd_decile
            FROM graveyards
            ORDER BY id
            """
        )

        rows = []
        for (
            gid,
            name,
            lat,
            lng,
            area_ha,
            ndvi_mean,
            carbon_total,
            carbon_per_ha,
            edi_norm,
            simd_rank,
            simd_decile,
        ) in cur:
            rows.append(
                {
                    "id": gid,
                    "name": name,
                    "latitude": float(lat) if lat is not None else None,
                    "longitude": float(lng) if lng is not None else None,
                    "areaHectares": float(area_ha) if area_ha is not None else None,
                    "ndvi": {
                        "meanNdvi": float(ndvi_mean) if ndvi_mean is not None else None,
                    }
                    if ndvi_mean is not None
                    else None,
                    "carbon": {
                        "totalCarbonTonnes": float(carbon_total)
                        if carbon_total is not None
                        else None,
                        "carbonPerHectare": float(carbon_per_ha)
                        if carbon_per_ha is not None
                        else None,
                    }
                    if carbon_total is not None or carbon_per_ha is not None
                    else None,
                    "deprivation": {
                        "ediScore": float(edi_norm) if edi_norm is not None else None,
                        "simdRank": int(simd_rank) if simd_rank is not None else None,
                        "simdQuintile": int(simd_decile)
                        if simd_decile is not None
                        else None,
                    }
                    if edi_norm is not None
                    or simd_rank is not None
                    or simd_decile is not None
                    else None,
                }
            )

        return rows
    finally:
        conn.close()

@app.route("/api/graveyards")
def api_graveyards():
    data = fetch_graveyards()
    return jsonify(data)

if __name__ == "__main__":
    # 开发调试用：python3 app.py
    app.run(host="0.0.0.0", port=55429, debug=True)