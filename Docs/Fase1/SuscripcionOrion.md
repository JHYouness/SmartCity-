### Crear una Suscripción en Orion para QuantumLeap
---
1. Crear una nueva solicitud POST a:
```sql
http://localhost:1026/v2/subscriptions
```

2. En Headers:
```sql
Key: Content-Type
Value: application/json
```

3. En Body (raw), copia:
```sql
{
  "description": "Suscripción a cambios en sensores",
  "subject": {
    "entities": [{ "idPattern": "Sensor.*", "type": "Sensor" }]
  },
  "notification": {
    "http": { "url": "http://quantumleap:8668/v2/notify" },
    "attrs": ["temperature", "humidity", "co2", "ph", "chlorine"]
  }
}

```
