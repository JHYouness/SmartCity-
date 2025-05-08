### Modifico la suscripcion, ya que debe incluir "metadata": ["TimeInstant"] para que QuantumLeap reciba esa marca temporal 

```sql
curl -X POST http://localhost:1026/v2/subscriptions \
  -H 'Content-Type: application/json' \
  -d '{
    "description": "Suscripción SmartCity → QL",
    "subject": { "entities": [{ "idPattern": "Sensor.*", "type": "Sensor" }] },
    "notification": {
      "http": { "url": "http://quantumleap:8668/v2/notify" },
      "attrs": ["temperature","humidity","co2","ph","chlorine"],
      "metadata": ["TimeInstant"]
    }
  }'
```
---
### Verificar que QuantumLeap ha recibido los datos
```sql
# Temperatura del SensorTemp1
curl -X GET "http://localhost:8668/v2/entities/SensorTemp1/attrs/temperature?type=Number" \
     -H "Accept: application/json"

# CO₂ del SensorCO2
curl -X GET "http://localhost:8668/v2/entities/SensorCO2/attrs/co2?type=Number" \
     -H "Accept: application/json"

# pH del SensorAgua
curl -X GET "http://localhost:8668/v2/entities/SensorAgua/attrs/ph?type=Number" \
     -H "Accept: application/json"
```
