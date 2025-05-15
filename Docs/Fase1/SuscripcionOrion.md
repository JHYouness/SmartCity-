### Crear una Suscripción en Orion para QuantumLeap
---

```sql
curl -X POST http://localhost:1026/v2/subscriptions \
  -H "Content-Type: application/json" \
  -d '{
    "description": "SmartCity → QuantumLeap",
    "subject": {
      "entities": [
        { "idPattern": "Sensor.*" }
      ],
      "condition": {
        "attrs": ["temperature", "humidity", "co2", "ph", "chlorine"]
      }
    },
    "notification": {
      "http": { "url": "http://quantumleap:8668/v2/notify" },
      "attrs": ["temperature", "humidity", "co2", "ph", "chlorine"],
      "metadata": ["TimeInstant"],
      "attrsFormat": "normalized"
    }
  }'


```
