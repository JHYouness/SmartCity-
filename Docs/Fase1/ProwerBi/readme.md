
# 🔷 VISUAL 1: Heatmap (Mapa de calor por día y sensor)
## Objetivo: ver claramente si hubo días críticos o valores anómalos

| Campo                   | Valor                           |
| ----------------------  | ------------------------------- |
| **Visualización**       | `Grafico de matriz de calor`    |
| **Eje X**               | `fecha_legible`                 |
| **Eje Y**               | `entity_id:5432`                |
| **Valores**             | `avg_value`                     |

🔷 FILTROS
- Segmentación de rango de fechas con fecha_legible
  
![Captura de pantalla (487)](https://github.com/user-attachments/assets/b8699978-386e-4c37-9409-6c82373778d7)

# 🔷 VISUAL 2: Grafico de lineas
## Objetivo: Ver cómo evolucionan los distintos atributos ambientales a lo largo del tiempo

| Campo                   | Valor                           |
| ----------------------  | ------------------------------- |
| **Visualización**       | `Grafico de lineas multiples`    |
| **Eje X**               | `fecha_legible (por día)`                 |
| **Eje Y**               | `avg_value (promedio diario)`                |
| **Leyenda**             | `attribute`                     |

🔷 FILTROS
- Segmentación con attriubute y entity_id, podiendo filtral:
  - Expandir o colapsar cada sensor (SensorAgua, SensorCO2, SensorTemp1)
  - Seleccionar individualmente los atributos que quiere ver de cada sensor



  ![Captura de pantalla (490)](https://github.com/user-attachments/assets/26fdb6a2-c684-472c-b424-79f71a07b375)
