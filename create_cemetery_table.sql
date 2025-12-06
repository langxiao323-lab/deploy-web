-- Drop existing table if it exists
DROP TABLE graveyards CASCADE CONSTRAINTS;

-- Create the graveyards table
CREATE TABLE graveyards (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR2(100) NOT NULL UNIQUE,
    strata VARCHAR2(20),
    area_m2 NUMBER,
    area_hectares NUMBER(10,4),
    lidar_mean_m NUMBER(10,2),
    canopy_percentage NUMBER(10,2),
    agb_total NUMBER(10,2),
    agb_per_hectare NUMBER(10,2),
    carbon_total_tonnes NUMBER(10,2),
    carbon_per_hectare_calibrate NUMBER(10,2),
    carbon_per_hectare_validate NUMBER(10,2),
    carbon_per_hectare NUMBER(10,2),
    potential_carbon_tonnes NUMBER(10,2),
    potential_carbon_ha NUMBER(10,2),
    ndvi_mean NUMBER(10,4),
    simd_rank NUMBER,
    simd_decile NUMBER,
    edi_simple NUMBER(10,2),
    edi_new_canopy_ndvi NUMBER(10,2),
    edi_new_2 NUMBER(10,2),
    norm_edi NUMBER(10,2),
    edi_norm NUMBER(10,2),
    created_date DATE DEFAULT SYSDATE
);

-- Create index on name for faster lookups
CREATE INDEX idx_graveyard_name ON graveyards(name);

COMMIT;

SELECT 'Table graveyards created successfully!' AS status FROM DUAL;
