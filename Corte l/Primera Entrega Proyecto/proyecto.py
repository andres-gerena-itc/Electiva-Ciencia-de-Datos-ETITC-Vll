# ANDRÉS FELIPE GERENA CONTRERAS - TS7A
# FABIÁN ESTEBAN SUAREZ ESTUPIÑAN - TS7A
# LAURA CAMILA MOSQUERA GONZALEZ - TS7A

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Definimos las regiones y sus características ideales
data = {
    "Región": ["La Guajira", "Cesar", "Antioquia", "Santander", "Córdoba"],
    "Irradiación (kWh/m²/año)": [2000, 1900, 1600, 1700, 1800],  # Datos ideales de irradiación
    "Costo de Instalación ($/kWp)": [1200, 1150, 1300, 1250, 1100],  # Costo de instalación ideal
    "Área de Paneles (m²)": [100, 100, 100, 100, 100]  # Área constante para simplificar
}

# Convertimos los datos en un DataFrame
df = pd.DataFrame(data)

# Se supone que hay una eficiencia promedio de paneles solares
eficiencia_promedio = 0.15  # 15%

# Calculamos la energía generada
df["Energía Generada (kWh/año)"] = (
    df["Irradiación (kWh/m²/año)"] * df["Área de Paneles (m²)"] * eficiencia_promedio
)

# Mostramos el DataFrame
print(df)

# Graficamos los resultados
plt.figure(figsize=(12, 6))
plt.bar(df["Región"], df["Energía Generada (kWh/año)"], color='skyblue')
plt.title('Energía Generada Ideal en Diferentes Regiones de Colombia')
plt.xlabel('Región')
plt.ylabel('Energía Generada (kWh/año)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Guardamos los resultados en un archivo CSV
df.to_csv('resultados_energia_ideal_colombia.csv', index=False)
