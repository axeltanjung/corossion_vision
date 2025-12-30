CREATE TABLE assets (
  asset_id TEXT PRIMARY KEY,
  type TEXT,
  location TEXT
);

CREATE TABLE inspections (
  id SERIAL PRIMARY KEY,
  asset_id TEXT,
  ts TIMESTAMPTZ DEFAULT now(),
  rust_area FLOAT,
  entropy FLOAT,
  corrosion_index FLOAT
);

SELECT create_hypertable('inspections','ts');
