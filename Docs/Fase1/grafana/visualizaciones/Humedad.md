```sql
SELECT
  time_index AS "time",
  humidity AS value
FROM doc.etsensor
WHERE entity_id = 'SensorTemp1'
ORDER BY time_index
```
![image](https://github.com/user-attachments/assets/8ff8061c-91b1-4d3a-857b-0d9d0a9667a3)
