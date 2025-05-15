## Entidades a traves de Postman
---
1. Sensor de temperatura que mide Temperatura y Humedad
```sql
curl -X POST http://localhost:1026/v2/entities \
  -H "Content-Type: application/json" \
  -d '{
    "id": "SensorTemp1",
    "type": "Sensor",
    "temperature": { "value": 25, "type": "Number" },
    "humidity": { "value": 60, "type": "Number" },
    "timestamp": { "value": "2025-03-01T00:00:00Z", "type": "DateTime" }
  }'
```

2. Sensor de CO2
```sql
curl -X POST http://localhost:1026/v2/entities \
  -H "Content-Type: application/json" \
  -d '{
    "id": "SensorCO2",
    "type": "Sensor",
    "co2": { "value": 400, "type": "Number" },
    "timestamp": { "value": "2025-03-01T00:00:00Z", "type": "DateTime" }
  }'
```

3. Sensor de calidad del agua que mide: PH, Temperatura y Cloro
```sql
curl -X POST http://localhost:1026/v2/entities \
  -H "Content-Type: application/json" \
  -d '{
    "id": "SensorAgua",
    "type": "Sensor",
    "ph": { "value": 7.5, "type": "Number" },
    "temperature": { "value": 20, "type": "Number" },
    "chlorine": { "value": 1.0, "type": "Number" },
    "timestamp": { "value": "2025-03-01T00:00:00Z", "type": "DateTime" }
  }'

```
