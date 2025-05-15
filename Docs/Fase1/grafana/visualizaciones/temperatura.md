```sql
SELECT
  time_index AS "time",
  temperature AS value
FROM doc.etsensor
WHERE entity_id = 'SensorTemp1'
ORDER BY time_index
```
![image](https://github.com/user-attachments/assets/33437fbb-b173-41e0-8d64-53d64f759630)
