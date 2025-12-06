-- Insert cemetery data from Cemeteries_Analysis.csv
-- Clear existing data
DELETE FROM graveyards;

-- Insert 35 cemeteries
INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Sciennes Jewish', 'Medium', 41, 0.00, 5.18, 58.54, 303.44, 74010.69, 151.72, 158.23, 74.55, 37005.34, 151.72, 37005.34, 0.11, 6721, 10, 58.65, 6.53, 33.87, 0.00, 5.97);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('St Mary''s Ratho', 'Low', 64, 0.01, 2.82, 26.56, 74.97, 11713.79, 37.48, 97.22, 51.12, 5856.90, 37.48, 5856.90, 0.51, 6328, 10, 27.08, 13.62, 38.43, 1.37, 6.89);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Mount Alvernia Convent', 'High', 667, 0.07, 1.71, 60.12, 103.01, 1544.32, 51.50, 68.53, 40.10, 772.16, 51.50, 772.16, 0.26, 6701, 10, 60.38, 15.33, 26.27, -2.27, 4.44);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Kirkliston Cemetery', 'Low', 1234, 0.12, 1.85, 11.95, 22.11, 179.16, 11.05, 72.14, 41.49, 89.58, 11.05, 89.58, 0.33, 3132, 5, 12.28, 3.91, 7.24, -7.97, 0.59);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Wauchope and Niddrie Village Graveyard', 'Medium', 1316, 0.13, 4.55, 55.02, 250.27, 1901.73, 125.13, 141.94, 68.29, 950.86, 125.13, 950.86, 0.38, 164, 1, 55.39, 20.78, 94.54, 18.15, 18.23);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Gogar', 'Medium', 1558, 0.16, 2.65, 59.31, 157.01, 1007.77, 78.50, 92.83, 49.43, 503.88, 78.50, 503.88, 0.49, 4580, 7, 59.80, 29.07, 76.97, 12.89, 14.68);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Duddingston', 'Medium', 1633, 0.16, 8.83, 51.07, 450.79, 2760.51, 225.40, 252.59, 110.79, 1380.26, 225.40, 1380.26, 0.41, 5729, 9, 51.48, 20.92, 184.69, 45.12, 36.44);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Buccleuch', 'Low', 1737, 0.17, 4.42, 28.90, 127.87, 736.14, 63.93, 138.58, 67.00, 368.07, 63.93, 368.07, 0.24, 4156, 6, 29.14, 6.94, 30.69, -0.95, 5.33);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('North Leith Burial Ground', 'High', 2520, 0.25, 7.14, 67.06, 478.67, 1899.49, 239.34, 208.90, 94.01, 949.74, 239.34, 949.74, 0.32, 715, 2, 67.38, 21.37, 152.51, 35.49, 29.94);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('St Triduana''s', 'Low', 2597, 0.26, 1.50, 19.98, 29.89, 115.08, 14.94, 63.10, 38.01, 57.54, 15.42, 59.36, 0.26, 5348, 8, 20.25, 5.26, 7.87, -7.78, 0.72);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Cramond Kirk', 'Low', 3517, 0.35, 2.09, 21.78, 45.42, 129.15, 22.71, 78.35, 43.87, 64.58, 22.71, 64.58, 0.45, 6845, 10, 22.23, 9.85, 20.55, -3.99, 3.28);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Old Calton Burial Ground', 'Medium', 4228, 0.42, 3.84, 45.27, 173.96, 411.45, 86.98, 123.59, 61.24, 205.72, 86.98, 205.72, 0.31, 3285, 5, 45.58, 13.99, 53.75, 5.95, 9.99);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Colinton Cemetery (churchyard)', 'Medium', 4570, 0.46, 4.90, 50.98, 249.76, 546.52, 124.88, 150.99, 71.77, 273.26, 124.88, 273.26, 0.43, 6735, 10, 51.41, 21.85, 107.04, 21.89, 20.75);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('South Leith Church', 'Medium', 7460, 0.75, 5.49, 48.08, 264.20, 354.16, 132.10, 166.24, 77.63, 177.08, 132.10, 177.08, 0.32, 1171, 2, 48.41, 15.49, 85.11, 15.33, 16.32);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Ratho Cemetery', 'Low', 7590, 0.76, 0.77, 13.21, 10.15, 13.38, 5.08, 44.22, 30.76, 6.69, 45.06, 59.36, 0.42, 6399, 10, 13.63, 5.59, 4.30, -8.85, 0.00);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Currie', 'Low', 8336, 0.83, 1.71, 8.21, 14.04, 16.84, 7.02, 68.53, 40.10, 8.42, 49.49, 59.36, 0.39, 5442, 8, 8.60, 3.20, 5.47, -8.50, 0.24);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Canongate Kirkyard', 'Low', 9503, 0.95, 3.33, 33.87, 112.83, 118.73, 56.41, 110.40, 56.18, 59.36, 56.41, 59.36, 0.32, 2611, 4, 34.19, 10.69, 35.59, 0.51, 6.32);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('East Preston Street Cemetery', 'Low', 9808, 0.98, 4.97, 27.79, 138.27, 140.97, 69.13, 152.80, 72.46, 70.49, 69.13, 70.49, 0.33, 6545, 10, 28.13, 9.31, 46.32, 3.72, 8.49);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('New Calton Burial Ground', 'Low', 11971, 1.20, 1.79, 19.85, 35.46, 29.62, 17.73, 70.59, 40.89, 14.81, 71.07, 59.36, 0.44, 2611, 4, 20.28, 8.64, 15.43, -5.52, 2.25);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Greyfiars Kirkyard', 'Medium', 12638, 1.26, 3.84, 37.81, 145.04, 114.76, 72.52, 123.59, 61.24, 57.38, 75.02, 59.36, 0.32, 4105, 6, 38.13, 12.16, 46.66, 3.83, 8.56);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('St Cuthbert', 'Medium', 18715, 1.87, 7.30, 54.35, 396.49, 211.86, 198.25, 213.04, 95.60, 105.93, 198.25, 105.93, 0.38, 4824, 7, 54.73, 20.79, 151.64, 35.23, 29.76);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Dalry Cemetery', 'High', 22316, 2.23, 0.54, 76.27, 40.93, 18.34, 20.47, 38.28, 28.48, 9.17, 132.48, 59.36, 0.44, 4505, 7, 76.71, 33.89, 18.19, -4.69, 2.81);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Mortonhall Cemetery', 'Low', 24996, 2.50, 3.49, 20.72, 72.33, 28.94, 36.17, 114.54, 57.77, 14.47, 148.39, 59.36, 0.41, 5447, 8, 21.13, 8.51, 29.71, -1.24, 5.13);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Liberton Cemetery', 'Low', 25820, 2.58, 1.85, 12.65, 23.40, 9.06, 11.70, 72.14, 41.49, 4.53, 153.28, 59.36, 0.33, 4955, 8, 12.98, 4.20, 7.77, -7.81, 0.70);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Comely Bank Cemetery', 'High', 27334, 2.73, 4.90, 60.39, 295.81, 108.22, 147.91, 150.99, 71.77, 54.11, 162.27, 59.36, 0.44, 6596, 10, 60.83, 26.86, 131.59, 29.23, 25.71);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Saughton Cemetery', 'Medium', 28066, 2.81, 4.91, 39.11, 192.21, 68.49, 96.11, 151.25, 71.87, 34.24, 166.61, 59.36, 0.43, 5702, 9, 39.54, 16.77, 82.43, 14.53, 15.78);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Portobello Cemetery', 'Low', 30874, 3.09, 2.50, 33.66, 84.12, 27.25, 42.06, 88.95, 47.94, 13.62, 183.28, 59.36, 0.41, 4538, 7, 34.06, 13.67, 34.17, 0.09, 6.03);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Corstorphine Hill Cemetery', 'High', 34528, 3.45, 7.77, 68.50, 532.01, 154.08, 266.01, 225.19, 100.26, 77.04, 266.01, 77.04, 0.50, 1033, 2, 69.00, 33.92, 263.42, 68.68, 52.34);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('North Merchiston Cemetery', 'High', 37167, 3.72, 7.11, 60.88, 432.73, 116.43, 216.37, 208.12, 93.71, 58.21, 220.64, 59.36, 0.47, 5001, 8, 61.35, 28.59, 203.21, 50.66, 40.18);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Rosebank Cemetery', 'Low', 43439, 4.34, 2.88, 25.96, 74.63, 17.18, 37.32, 98.77, 51.71, 8.59, 257.87, 59.36, 0.34, 6638, 10, 26.30, 8.93, 25.67, -2.45, 4.32);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Grange Cemetery', 'Medium', 46688, 4.67, 6.26, 37.55, 235.14, 50.36, 117.57, 186.15, 85.27, 25.18, 277.16, 59.36, 0.44, 6617, 10, 37.99, 16.44, 102.93, 20.66, 19.92);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Morningside Cemetery', 'Low', 54516, 5.45, 1.16, 28.28, 32.70, 6.00, 16.35, 54.31, 34.64, 3.00, 323.63, 59.36, 0.46, 6768, 10, 28.73, 12.92, 14.94, -5.66, 2.15);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Newington Cemetery', 'High', 55647, 5.56, 12.16, 83.36, 1013.63, 182.15, 506.82, 338.68, 143.85, 91.08, 506.82, 91.08, 0.49, 6416, 10, 83.85, 41.07, 499.38, 139.27, 100.00);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Craigmillar Castle Park Cemetery', 'Low', 57754, 5.78, 8.62, 24.08, 207.47, 35.92, 103.74, 247.16, 108.70, 17.96, 342.85, 59.36, 0.45, 1380, 2, 24.53, 10.92, 94.06, 18.01, 18.13);

INSERT INTO graveyards (name, strata, area_m2, area_hectares, lidar_mean_m, canopy_percentage, agb_total, agb_per_hectare, carbon_total_tonnes, carbon_per_hectare_calibrate, carbon_per_hectare_validate, carbon_per_hectare, potential_carbon_tonnes, potential_carbon_ha, ndvi_mean, simd_rank, simd_decile, edi_simple, edi_new_canopy_ndvi, edi_new_2, norm_edi, edi_norm)
VALUES ('Warriston Cemetery', 'High', 83620, 8.36, 9.79, 71.87, 703.22, 84.10, 351.61, 277.41, 120.32, 42.05, 496.41, 59.36, 0.52, 6062, 9, 72.39, 37.62, 368.12, 100.00, 73.49);

COMMIT;

-- Verify data
SELECT COUNT(*) AS total_cemeteries FROM graveyards;
SELECT name, strata, carbon_per_hectare_validate AS carbon, simd_decile, edi_norm 
FROM graveyards 
ORDER BY carbon_per_hectare_validate DESC 
FETCH FIRST 10 ROWS ONLY;

SELECT 'Data inserted successfully! Total cemeteries: ' || COUNT(*) AS status FROM graveyards;
