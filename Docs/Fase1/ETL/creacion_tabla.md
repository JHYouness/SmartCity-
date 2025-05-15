# Creacion de tabla
```sql
CREATE TABLE IF NOT EXISTS doc.dw_sensor_resumen (
  entity_id TEXT,
  attribute TEXT,
  date TIMESTAMP,
  min_value DOUBLE,
  max_value DOUBLE,
  avg_value DOUBLE,
  PRIMARY KEY (entity_id, attribute, date)
);
```
