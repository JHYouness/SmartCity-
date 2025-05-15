# 🏙️ Smart City - Proyecto Fase 1

Este proyecto simula el funcionamiento de una ciudad inteligente utilizando la plataforma **FIWARE**, enfocándose en la captura, almacenamiento y visualización de datos de sensores.

---

## 📦 Tecnologías utilizadas

- **FIWARE Orion Context Broker**
- **QuantumLeap**
- **CrateDB**
- **Grafana**
- **Power BI**
- **Python (para ingesta de datos)**
- **Docker + docker-compose**

---

## 🎯 Objetivo general

Simular una Smart City en la que tres sensores virtuales generan datos que se almacenan en una base de datos de series temporales, se visualizan en un dashboard (Grafana) y se resumen en un Data Warehouse para su análisis en Power BI.

---

## 🧭 Estructura del proyecto

```bash
Docs/
└── Fase1/
    ├── ETL/
    │   ├── creacion_tabla.md
    │   ├── ingesta.md
    │   ├── verificacion.md
    ├── grafana/
    │   ├── configuracion.md
    │   ├── variable.md
    │   └── visualizaciones/
    │       ├── temperatura.md
    │       ├── CO₂.md
    │       ├── Humedad.md
    │       └── pH.md
    ├── Entidades.md
    ├── SuscripcionOrion.md
    ├── IngestaDatos.py
    ├── documentacion.md
README.md
