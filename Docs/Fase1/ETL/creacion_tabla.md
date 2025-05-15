# Creacion de tabla
Primero hay que entrar en el contendor de create, para ello:
```sql
docker exec -it crate bash
```
Una vez dentro ejecutar:
```sql
crash
```

Ahora si, crear la tabla:
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
