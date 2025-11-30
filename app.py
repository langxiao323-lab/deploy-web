#!/usr/bin/env python3
import sys
import json
import cx_Oracle

print("Content-Type: application/json")
print("Access-Control-Allow-Origin: *")
print()

ORACLE_USER = "s2835812"
ORACLE_PASSWORD = "252525"
ORACLE_DSN = "GEOSLEARN"

conn = cx_Oracle.connect(
    user=ORACLE_USER,
    password=ORACLE_PASSWORD,
    dsn=ORACLE_DSN
)

cur = conn.cursor()
cur.execute("""
    SELECT 
        id, name, latitude, longitude,
        area_hectares,
        ndvi_mean,
        carbon_total_tonnes, carbon_per_hectare,
        edi_norm, simd_rank, simd_decile
    FROM graveyards
    ORDER BY id
""")

rows = cur.fetchall()
cur.close()
conn.close()

result = []
for row in rows:
    (gid, name, lat, lon, area,
     ndvi_mean,
     carbon_total, carbon_per_ha,
     edi_norm, simd_rank, simd_decile) = row
    
    result.append({
        "id": gid,
        "name": name,
        "latitude": float(lat) if lat is not None else None,
        "longitude": float(lon) if lon is not None else None,
        "areaHectares": float(area) if area is not None else None,
        "ndvi": {
            "meanNdvi": float(ndvi_mean) if ndvi_mean is not None else None
        },
        "carbon": {
            "totalCarbonTonnes": float(carbon_total) if carbon_total is not None else None,
            "carbonPerHectare": float(carbon_per_ha) if carbon_per_ha is not None else None
        },
        "deprivation": {
            "ediScore": float(edi_norm) if edi_norm is not None else None,
            "simdRank": int(simd_rank) if simd_rank is not None else None,
            "simdScore": float(simd_decile * 10) if simd_decile is not None else None
        }
    })

print(json.dumps(result, indent=2))
