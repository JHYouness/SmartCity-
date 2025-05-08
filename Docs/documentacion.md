# Fase 1

## Entidades a traves de Postman
1. Sensor de temperatura que mide Temperatura y Humedad
```sql
{
  "id": "SensorTemp1",
  "type": "Sensor",
  "temperature": { "value": 25, "type": "Number" },
  "humidity": { "value": 60, "type": "Number" }
}
```

2. Sensor de CO2
```sql

{
  "id": "SensorCO2",
  "type": "Sensor",
  "co2": { "value": 400, "type": "Number" }
}
```

3. Sensor de calidad del agua que mide: PH, Temperatura y Cloro
```sql
{
  "id": "SensorAgua",
  "type": "Sensor",
  "ph": { "value": 7.5, "type": "Number" },
  "temperature": { "value": 20, "type": "Number" },
  "chlorine": { "value": 1.0, "type": "Number" }
}
```
