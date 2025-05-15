import requests
import random
from datetime import datetime, timedelta

# Configuración
ORION_URL = 'http://localhost:1026/v2/entities'
HEADERS = {'Content-Type': 'application/json'}
START_DATE = datetime(2025, 3, 1)
END_DATE = datetime(2025, 4, 30, 23, 59)
READINGS = 400

# Sensores y atributos con rangos realistas
SENSORS = {
    'SensorTemp1': {
        'temperature': (18, 30),
        'humidity': (30, 80)
    },
    'SensorCO2': {
        'co2': (300, 600)
    },
    'SensorAgua': {
        'ph': (6.5, 8.5),
        'temperature': (10, 25),
        'chlorine': (0.5, 2.0)
    }
}

# Generador de timestamps únicos en el rango
def generate_timestamps(start, end, count):
    total_seconds = int((end - start).total_seconds())
    timestamps = set()
    while len(timestamps) < count:
        ts = start + timedelta(seconds=random.randint(0, total_seconds))
        timestamps.add(ts)
    return sorted(timestamps)

# Enviar PATCH a Orion
def send_patch(entity_id, attributes, timestamp):
    iso_time = timestamp.isoformat() + 'Z'
    payload = {}

    for attr, (low, high) in attributes.items():
        value = round(random.uniform(low, high), 2)
        payload[attr] = {
            'value': value,
            'type': 'Number',
            'metadata': {
                'TimeInstant': {
                    'type': 'DateTime',
                    'value': iso_time
                }
            }
        }

    # Atributo extra para ver la fecha en Orion (opcional)
    payload["timestamp"] = {
        "value": iso_time,
        "type": "DateTime"
    }

    url = f"{ORION_URL}/{entity_id}/attrs"
    res = requests.patch(url, headers=HEADERS, json=payload)

    if res.status_code not in [204, 200]:
        print(f"[{res.status_code}] Error for {entity_id} at {iso_time}: {res.text}")

# Ejecutar el envío
def main():
    for entity_id, attrs in SENSORS.items():
        print(f"📡 Insertando 400 lecturas para {entity_id}")
        timestamps = generate_timestamps(START_DATE, END_DATE, READINGS)
        for ts in timestamps:
            send_patch(entity_id, attrs, ts)
    print("✅ ¡Carga histórica completada!")

if __name__ == '__main__':
    main()
