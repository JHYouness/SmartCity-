# Insertar los valores agregados
## 🔹 Temperatura (SensorTemp1 y SensorAgua)
```sql
INSERT INTO doc.dw_sensor_resumen
SELECT
  entity_id,
  'temperature' AS attribute,
  DATE_TRUNC('day', time_index) AS date,
  MIN(temperature),
  MAX(temperature),
  AVG(temperature)
FROM doc.etsensor
WHERE temperature IS NOT NULL
GROUP BY entity_id, DATE_TRUNC('day', time_index);
```
## 🔹 Humedad (SensorTemp1)
```sql
INSERT INTO doc.dw_sensor_resumen
SELECT
  entity_id,
  'humidity' AS attribute,
  DATE_TRUNC('day', time_index) AS date,
  MIN(humidity),
  MAX(humidity),
  AVG(humidity)
FROM doc.etsensor
WHERE humidity IS NOT NULL
GROUP BY entity_id, DATE_TRUNC('day', time_index);
```

## 🔹 CO₂ (SensorCO2)
```sql
INSERT INTO doc.dw_sensor_resumen
SELECT
  entity_id,
  'co2' AS attribute,
  DATE_TRUNC('day', time_index) AS date,
  MIN(co2),
  MAX(co2),
  AVG(co2)
FROM doc.etsensor
WHERE co2 IS NOT NULL
GROUP BY entity_id, DATE_TRUNC('day', time_index);
```
 ## 🔹 pH (SensorAgua)
```sql
INSERT INTO doc.dw_sensor_resumen
SELECT
  entity_id,
  'ph' AS attribute,
  DATE_TRUNC('day', time_index) AS date,
  MIN(ph),
  MAX(ph),
  AVG(ph)
FROM doc.etsensor
WHERE ph IS NOT NULL
GROUP BY entity_id, DATE_TRUNC('day', time_index);
```

## 🔹 Cloro (SensorAgua)
```sql
INSERT INTO doc.dw_sensor_resumen
SELECT
  entity_id,
  'chlorine' AS attribute,
  DATE_TRUNC('day', time_index) AS date,
  MIN(chlorine),
  MAX(chlorine),
  AVG(chlorine)
FROM doc.etsensor
WHERE chlorine IS NOT NULL
GROUP BY entity_id, DATE_TRUNC('day', time_index);
```
