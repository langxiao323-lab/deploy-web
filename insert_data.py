#!/usr/bin/env python3
import json
import math
import cx_Oracle

ORACLE_USER = "s2835812"
ORACLE_PASSWORD = "252525"
ORACLE_DSN = "GEOSLEARN"

EDINBURGH_CENTER = {"lat": 55.9533, "lng": -3.1883}


def generate_coordinates(index: int, total: int):
    radius = 0.06
    angle = (index / total) * 2 * math.pi
    distance = 0.03
    return {
        "lat": EDINBURGH_CENTER["lat"] + distance * math.cos(angle),
        "lng": EDINBURGH_CENTER["lng"] + distance * math.sin(angle),
    }


def main():
    # 1) 读取 Lidarr.json（注意：路径相对于仓库根目录）
    with open("Lidarr.json", "r", encoding="utf-8") as f:
        raw = json.load(f)

    rows = [g for g in raw if "Cemetery" in g and g["Cemetery"]]
    print(f"准备插入 {len(rows)} 条墓地记录")

    conn = cx_Oracle.connect(
        user=ORACLE_USER,
        password=ORACLE_PASSWORD,
        dsn=ORACLE_DSN,
    )
    cur = conn.cursor()

    # 2) 清空旧数据
    cur.execute("DELETE FROM graveyards")
    conn.commit()

    for i, g in enumerate(rows):
        coords = generate_coordinates(i, len(rows))

        name = g.get("Cemetery")
        area_m2 = g.get("Area (m2)")
        area_ha = g.get("Area (hectare)")
        lidar_mean = g.get("LiDAR Mean (m)")
        canopy_pct = g.get("Canopy Percentage (%)")
        agb_total = g.get("AGB total")
        agb_per_ha = g.get("AGB per hectare")
        carbon_total = g.get("Carbon total (tonnes)")
        carbon_per_ha = g.get("Carbon per hectare")
        potential_carbon = g.get("Potential carbon ha-1")
        ndvi_mean = g.get("NDVI Mean")
        simd_rank = g.get("SIMD Rank")
        simd_decile = g.get("SIMD Decile")
        edi_simple = g.get("EDI simple")
        edi_new_canopy = g.get("EDI new (Canopy % x NDVI)")
        edi_new_2 = g.get("EDI new 2")
        norm_edi = g.get("Norm. EDI")
        edi_norm = g.get("EDI norm.")
        strata = g.get("Strata")

        cur.execute(
            """
            INSERT INTO graveyards (
              name, latitude, longitude,
              area_m2, area_hectares,
              lidar_mean_m, canopy_percentage,
              agb_total, agb_per_hectare,
              carbon_total_tonnes, carbon_per_hectare, potential_carbon_ha,
              ndvi_mean,
              simd_rank, simd_decile,
              edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm,
              strata
            ) VALUES (
              :name, :lat, :lng,
              :area_m2, :area_ha,
              :lidar_mean, :canopy_pct,
              :agb_total, :agb_per_ha,
              :carbon_total, :carbon_per_ha, :potential_carbon,
              :ndvi_mean,
              :simd_rank, :simd_decile,
              :edi_simple, :edi_new_canopy, :edi_new_2, :norm_edi, :edi_norm,
              :strata
            )
            """,
            dict(
                name=name,
                lat=coords["lat"],
                lng=coords["lng"],
                area_m2=area_m2,
                area_ha=area_ha,
                lidar_mean=lidar_mean,
                canopy_pct=canopy_pct,
                agb_total=agb_total,
                agb_per_ha=agb_per_ha,
                carbon_total=carbon_total,
                carbon_per_ha=carbon_per_ha,
                potential_carbon=potential_carbon,
                ndvi_mean=ndvi_mean,
                simd_rank=simd_rank,
                simd_decile=simd_decile,
                edi_simple=edi_simple,
                edi_new_canopy=edi_new_canopy,
                edi_new_2=edi_new_2,
                norm_edi=norm_edi,
                edi_norm=edi_norm,
                strata=strata,
            ),
        )

        if (i + 1) % 5 == 0:
            print(f"  已插入 {i+1} 条...")
            conn.commit()

    conn.commit()
    print("✅ 插入完成！")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()