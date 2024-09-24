## INTEGRANTES

1. ANDRÉS FELIPE GERENA CONTRERAS
2. FABIÁN ESTEBAN SUREZ ESTUPIÑAN
3. LAURA CAMILA MOSUQERA GONZALEZ

# Optimización de la Distribución de Recursos de Energía Solar en Colombia

## 1. Introducción
Colombia posee un gran potencial para la energía solar debido a su ubicación geográfica y condiciones climáticas. Este proyecto tiene como objetivo optimizar la ubicación de paneles solares en el país para maximizar la eficiencia y minimizar costos, contribuyendo así a la transición hacia fuentes de energía más sostenibles.

## 2. Planteamiento del Problema
El problema se centra en determinar las mejores ubicaciones para instalar paneles solares en Colombia, considerando factores como:

### Radiación solar: 
Diferencias en la irradiación a lo largo del país.
### Costos de instalación: 
Variaciones en costos de instalación y mantenimiento en diferentes regiones.
### Demanda energética: 
Áreas con alta demanda de energía que se beneficiarían más de la energía solar.

El objetivo es maximizar la generación de energía solar y la rentabilidad de la inversión.

## 3. Metodología
### 3.1. Recopilación de Datos
* Datos de Radiación Solar: Se planea utilizar el Global Solar Atlas para obtener datos sobre irradiación solar en Colombia.
* Datos de Infraestructura: Se Investigarán los costos de instalación de paneles solares en diferentes departamentos colombianos.
* Datos de Demanda Energética: Obtener información sobre la demanda de energía a nivel departamental o municipal. Esto puede incluir datos del Ministerio de Minas y Energía de Colombia.
  
### 3.2. Modelo Matemático
* Función Objetivo: Maximizar la energía generada y minimización de costos.
La función objetivo podría estar representada como:

### Maximizar 𝐸 = ∑ 𝑖 = 1 𝑛 (𝛼𝑖 ⋅ 𝑃𝑖 − 𝛽𝑖 ⋅ 𝐶𝑖)


Donde:

* 𝐸 es la energía neta generada.
* 𝛼𝑖 es el coeficiente de eficiencia para el recurso en la ubicación 𝑖 (basado en datos climáticos).
* 𝑃𝑖 es la capacidad de generación en la ubicación 𝑖
* 𝛽𝑖 es el coeficiente de costo asociado a la ubicación 𝑖
* 𝐶𝑖 es el costo total de instalación y mantenimiento en 𝑖

### 3.3. Algoritmos de Optimización

* Optimización Estocástica: Usar simulación de Monte Carlo para considerar la variabilidad de la irradiación solar a lo largo del año.
* Programación Lineal/No Lineal: Para establecer restricciones y optimizar la asignación de recursos.
* Algoritmos Genéticos: Para encontrar combinaciones óptimas de ubicación y recursos.

## 4. Resultados Preliminares
Dentro del primer análisis se generó un programa en python que permite (con datos no reales) utilizando un modelo de optimización, simular la generación de energía solar en diversas regiones de Colombia, estos son datos "ideales" que deberían tener estas zonas del país, en futuros entregables se piensa utilizar Dataset reales para ser más concretos con el resultado del proyecto.

![image](https://github.com/user-attachments/assets/540ad508-68ee-481f-b7e0-616d7a675121)

### Descripción de Resultados:

* Irradiación Solar: Los valores de irradiación solar se obtuvieron del Global Solar Atlas y del IDEAM, mostrando que La Guajira presenta el mayor potencial de irradiación solar en el país.

* Costo de Instalación: Los costos de instalación se basaron en reportes de SER Colombia y IRENA, lo que indica que el costo de instalación varía según la región, siendo Córdoba la que presenta el costo más bajo.

* Energía Generada: La energía generada se calculó utilizando la fórmula:

### 𝐸 generada = Irradiación × Área de paneles × Eficiencia

Con una eficiencia promedio de paneles solares del 15%. Los resultados indican que La Guajira y Cesar son las regiones con mayor energía generada.

## 5. Conclusión y Próximos Pasos

### Conclusión: 

El análisis preliminar demuestra que ciertas regiones de Colombia, como La Guajira y Cesar, tienen un gran potencial para la generación de energía solar. Los datos ideales utilizados en este modelo se sustentan en fuentes confiables, lo que otorga solidez a los resultados obtenidos. Este estudio no solo evidencia la viabilidad de la energía solar en Colombia, sino que también proporciona una base para el desarrollo de un modelo más robusto que considere datos reales.

### Próximos Pasos:
* Incorporar Datos Reales: En futuras fases del proyecto, se buscarán datos reales de irradiación solar, costos de instalación y demanda energética para validar y ajustar el modelo.
* Análisis de Sensibilidad: Realizar un análisis de sensibilidad para determinar cómo diferentes variables (por ejemplo, cambios en costos de instalación o eficiencia de paneles) afectan la generación de energía.
* Expansión del Modelo: Considerar la integración de otras fuentes de energía renovable y la evaluación de su complementariedad con la energía solar.
* Desarrollo de Recomendaciones: Basado en el modelo optimizado, se elaborarán recomendaciones para la instalación de paneles solares en las regiones identificadas como más prometedoras.

### GRÁFICA (Figura 1), ENERGÍA GENERADA IDEAL EN DIFERENTES REGIONES DE COLOMBIA

![image](https://github.com/user-attachments/assets/ba7f0513-a230-45a8-a120-09477170ab1d)


Este informe inicial sienta las bases para un análisis más profundo y detallado que contribuirá al desarrollo de soluciones energéticas sostenibles en Colombia.


