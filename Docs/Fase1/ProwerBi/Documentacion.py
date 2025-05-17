# He realizado el proyecto en Fedora, para pasar los datos a la maquina virtual (Windows) y poder trabajar los datos en power bi he ejecutado el siguiente scipt 

import crate.client
import pandas as pd

# Conexión a CrateDB desde el host
connection = crate.client.connect("http://localhost:4200")
cursor = connection.cursor()

# Consulta a la tabla de resumen
cursor.execute("SELECT * FROM doc.dw_sensor_resumen")
rows = cursor.fetchall()

# Convertir a DataFrame
df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Exportar a CSV
df.to_csv("dw_sensor_resumen.csv", index=False)
print("✅ Archivo CSV exportado correctamente.")
