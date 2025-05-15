```sql
SELECT
  time_index AS "time",
  co2 AS value
FROM doc.etsensor
WHERE entity_id = 'SensorCO2'
ORDER BY time_index
```
![image](https://github.com/user-attachments/assets/e952df48-7a6c-43f0-87b2-7efb0eacfee2)
