CREATE TABLE graveyards (
  id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR2(200) NOT NULL,
  latitude NUMBER NOT NULL,
  longitude NUMBER NOT NULL,
  area_m2 NUMBER,
  area_hectares NUMBER,
  lidar_mean_m NUMBER,
  canopy_percentage NUMBER,
  agb_total NUMBER,
  agb_per_hectare NUMBER,
  carbon_total_tonnes NUMBER,
  carbon_per_hectare NUMBER,
  potential_carbon_ha VARCHAR2(200),
  ndvi_mean NUMBER,
  simd_rank NUMBER,
  simd_decile NUMBER,
  edi_simple NUMBER,
  edi_new_canopy_ndvi NUMBER,
  edi_new_2 NUMBER,
  norm_edi NUMBER,
  edi_norm NUMBER,
  strata VARCHAR2(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE INDEX idx_graveyard_name ON graveyards(name);
CREATE INDEX idx_graveyard_ndvi ON graveyards(ndvi_mean);
CREATE INDEX idx_graveyard_carbon ON graveyards(carbon_total_tonnes);
CREATE INDEX idx_graveyard_edi ON graveyards(edi_norm);
CREATE INDEX idx_graveyard_simd ON graveyards(simd_rank);

COMMIT;
