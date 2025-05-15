```sql
SELECT
  time_index AS "time",
  ph AS value
FROM doc.etsensor
WHERE entity_id = 'SensorAgua'
ORDER BY time_index
```

![image](https://github.com/user-attachments/assets/9ab07272-b334-4688-9b68-e7a8cfd98ec9)
