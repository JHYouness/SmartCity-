
# 🌆 Proyecto Smart City con FIWARE

## 1. ✨ Definición

Este proyecto simula una Smart City utilizando la plataforma FIWARE. Se definen y simulan tres sensores:

1. 🌡️ **Sensor de temperatura**: mide Temperatura y Humedad
2. 🟫 **Sensor de CO₂**
3. 💧 **Sensor de calidad del agua**: mide pH, Temperatura y Cloro

Se capturan datos de estos sensores y se almacenan mediante servicios de FIWARE (Orion, QuantumLeap, CrateDB), y se visualizan con Grafana y Power BI.

El proyecto se centra únicamente en la:

- ⚙️ **Fase 1**: Configuración de la infraestructura sin IoT-Agent, con servicios de persistencia (QuantumLeap y CrateDB)

## 2. 🔗 Enlaces a documentación

- [🔹 Uso avanzado NGSIv2](https://github.com/FIWAREZone/tutorial.ngsi-advanced)
- [🔹 Ejemplo de uso](https://fiware-training.readthedocs.io/es-mx/latest/casodeestudio/descripcion/)
- [🔹 Esquema de funcionamiento](https://fiware-tutorials.readthedocs.io/en/latest/getting-started.html)
- [🔹 Agentes IoT](https://github.com/FIWAREZone/tutorial.iot-agents)

## 3. 📄 Pasos del Proyecto y Estructura de Ficheros

### 🚀 Fase 1 - Infraestructura, Simulación de Datos y Visualización

1. **Definición de entidades**
   - [`Docs/Fase1/Entidades.md`](Docs/Fase1/Entidades.md)

2. **Creación de suscripciones en Orion**
   - [`Docs/Fase1/SuscripcionOrion.md`](Docs/Fase1/SuscripcionOrion.md)

3. **Ingesta de datos simulados**
   - [`Docs/Fase1/IngestaDatos.py`](Docs/Fase1/IngestaDatos.py)

4. **Configuración de Grafana**
   - [`Docs/Fase1/grafana/configuracion.md`](Docs/Fase1/grafana/configuracion.md)

5. **Visualizaciones en Grafana** 📊
   - [`Docs/Fase1/grafana/visualizaciones/CO₂.md`](Docs/Fase1/grafana/visualizaciones/CO₂.md)
   - [`Docs/Fase1/grafana/visualizaciones/Humedad.md`](Docs/Fase1/grafana/visualizaciones/Humedad.md)
   - [`Docs/Fase1/grafana/visualizaciones/pH.md`](Docs/Fase1/grafana/visualizaciones/pH.md)
   - [`Docs/Fase1/grafana/visualizaciones/temperatura.md`](Docs/Fase1/grafana/visualizaciones/temperatura.md)

6. **Variables en Grafana** 🔧
   - [`Docs/Fase1/grafana/variable.md`](Docs/Fase1/grafana/variable.md)

7. **ETL para Data Warehouse** 🛢️
   - Creación tabla: [`Docs/Fase1/ETL/creacion_tabla.md`](Docs/Fase1/ETL/creacion_tabla.md)
   - Ingesta: [`Docs/Fase1/ETL/ingesta.md`](Docs/Fase1/ETL/ingesta.md)
   - Verificación: [`Docs/Fase1/ETL/verificacion.md`](Docs/Fase1/ETL/verificacion.md)

8. **Visualizaciones en Power BI** 🔍
   - [`Docs/Fase1/ProwerBi/Visualizacion1.md`](Docs/Fase1/ProwerBi/Visualizacion1.md)
   - [`Docs/Fase1/ProwerBi/Visualizacion2.md`](Docs/Fase1/ProwerBi/Visualizacion2.md)

---

## 4. 🎯 Objetivo Final

- Desarrollar un entorno FIWARE funcional y documentado.
- Simular sensores y visualizar sus datos.
- Implementar una arquitectura de análisis de datos con Grafana, Power BI y Data Warehouse.
- Dejar documentado el proceso en markdowns para facilitar replicación o ampliación.

---

**👨‍🎓 Autores:** Proyecto de simulación educativa FIWARE Smart City.

**📂 Repositorio:** Este README resume los pasos y ficheros necesarios para ejecutar y comprender el proyecto.
