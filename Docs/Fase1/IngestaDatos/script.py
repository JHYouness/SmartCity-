#!/usr/bin/env python3
import requests, random
from datetime import datetime, timedelta

ORION = 'http://localhost:1026'
HEADERS = {'Content-Type': 'application/json'}
START = datetime(2025, 3, 1)
END   = datetime(2025, 4, 30, 23, 59, 59)
N = 400

SENSORS = {
    'SensorTemp1': {
        'temperature': (18.0, 30.0),
        'humidity':    (30.0, 80.0),
    },
    'SensorCO2': {
        'co2': (300, 600),
    },
    'SensorAgua': {
        'ph':          (6.5, 8.5),
        'temperature': (10.0, 25.0),
        'chlorine':    (0.5, 2.0),
    },
}

def random_timestamps(start, end, n):
    span = int((end - start).total_seconds())
    return sorted(start + timedelta(seconds=random.randint(0, span)) for _ in range(n))

def send_reading(eid, attrs, ts):
    iso = ts.isoformat() + 'Z'
    payload = {}
    for a, (lo, hi) in attrs.items():
        payload[a] = {
            'value': round(random.uniform(lo, hi), 2),
            'type': 'Number',
            'metadata': {
                'TimeInstant': {
                    'type': 'DateTime',
                    'value': iso
                }
            }
        }
    url = f"{ORION}/v2/entities/{eid}/attrs"
    r = requests.patch(url, headers=HEADERS, json=payload)
    if not (200 <= r.status_code < 300):
        print(f"[ERROR {r.status_code}] {eid} @ {iso}: {r.text}")

def main():
    for eid, attrs in SENSORS.items():
        print(f"Generando {N} lecturas para {eid}…")
        for ts in random_timestamps(START, END, N):
            send_reading(eid, attrs, ts)
    print("¡Terminado!")

if __name__ == '__main__':
    main()
