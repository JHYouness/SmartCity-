```sql
SELECT
  time_index AS "time",
  co2 AS value
FROM doc.etsensor
WHERE entity_id = 'SensorCO2'
ORDER BY time_index
```
