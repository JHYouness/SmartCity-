```sql
SELECT
  time_index AS "time",
  temperature AS value
FROM doc.etsensor
WHERE entity_id = 'SensorTemp1'
ORDER BY time_index
```
