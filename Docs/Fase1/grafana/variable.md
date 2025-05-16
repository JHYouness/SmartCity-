# Configuracion variable 

| Campo           | Valor                                                                            |
| --------------- | -------------------------------------------------------------------------------- |
| **Name**        | `sensor_temp`                                                                    |
| **Type**        | `Query`                                                                          |
| **Data source** | `CrateDB`                                    |
| **Query**       | `SELECT DISTINCT entity_id FROM doc.etsensor WHERE temperature IS NOT NULL ` |
| **Refresh**     | On Dashboard Load                                                                |

# Consulta utilizando la variable 
```sql
SELECT
  time_index AS "time",
  temperature AS value
FROM doc.etsensor
WHERE entity_id = '$sensor_temp'
ORDER BY time_index
```

![image](https://github.com/user-attachments/assets/07ac4790-71fa-40ec-8b84-37d57f350345)
