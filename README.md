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
```

---

## 🚦 Fase 1 - Simulación sin IoT Agent

### ✔️ Componentes

- 3 sensores simulados:
  - `SensorTemp1`: temperatura y humedad
  - `SensorCO2`: CO₂
  - `SensorAgua`: pH, temperatura y cloro
- Orion Context Broker + QuantumLeap + CrateDB + Grafana
- Script Python que envía 400 lecturas por atributo (marzo y abril 2025)

### ✔️ Requisitos cumplidos

✅ Creación de las entidades  
✅ Creación de la suscripción con metadata `TimeInstant`  
✅ Ingesta de datos históricos (01/03/25 - 30/04/25)  
✅ Visualización en Grafana: 4 paneles + 1 variable  
✅ ETL: resumen diario en tabla `dw_sensor_resumen`  
✅ Cuadro de mando en Power BI con 2 visualizaciones y 2 filtros  

---

## 📈 Fase 2 - Con Cygnus y MySQL (❌ aún no iniciado)

- Reemplazar QuantumLeap y CrateDB por:
  - FIWARE Cygnus como sistema de ingesta
  - MySQL como base de datos histórica
- Reconfigurar Orion para notificar a Cygnus

---

## 🌐 Fase 3 - Con IoT Agent y sensores reales (❌ aún no iniciado)

- Integrar un IoT Agent (Ultralight o JSON)
- Conectar con sensores reales o simulados por HTTP/MQTT
- Orion recibe datos automáticamente y los canaliza a almacenamiento

---

## 📄 Documentación

Cada parte del proyecto está explicada en los archivos `.md` organizados por categoría:

- `grafana/` → configuración, paneles, variable dinámica
- `ETL/` → creación de tabla, inserción de datos, verificación
- `Entidades.md` → definición de sensores
- `SuscripcionOrion.md` → configuración correcta de notificaciones

---

## 🚀 Cómo iniciar el proyecto

1. Clonar el repositorio
2. Lanzar los contenedores con:
   ```bash
   docker-compose up -d
   ```
3. Ejecutar el script de carga de datos:
   ```bash
   python IngestaDatos.py
   ```
4. Ver dashboards en:
   - Grafana: [http://localhost:3000](http://localhost:3000)
   - Power BI: conectar a CrateDB por PostgreSQL

---

## 🙋 Autor

Youness — Proyecto Smart City para Fase 1
