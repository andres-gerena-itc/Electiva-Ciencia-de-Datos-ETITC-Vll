URL CÓDIGO PYTHON EN GOOGLE COLAB PROYECTO: https://colab.research.google.com/drive/15txMfUOtt9vRe7O-tYBonvHVTVE6oNv1?usp=sharing

## INTEGRANTES

1. ANDRÉS FELIPE GERENA CONTRERAS
2. FABIÁN ESTEBAN SUAREZ ESTUPIÑAN
3. LAURA CAMILA MOSQUERA GONZALEZ

# Informe Visualización de Datos y Análisis Avanzado para la Optimización de Recursos de Energía Solar en Colombia

Para mejorar nuestro proyecto de optimización de recursos de energía solar en Colombia, hemos avanzado en el análisis mediante técnicas de visualización más sofisticadas, lo que nos ha permitido comprender mejor las variaciones en la irradiación, el costo de instalación y la energía generada en distintas regiones. A continuación, se describe el enfoque, los métodos y técnicas de visualización utilizados y los resultados preliminares obtenidos.

## Visualización de Datos
Las visualizaciones avanzadas permiten interpretar y comunicar los hallazgos de manera eficaz. Utilizamos Python y bibliotecas especializadas como Seaborn y Matplotlib para crear gráficos que muestran la relación entre los factores clave de generación de energía solar. Estas visualizaciones ofrecen una perspectiva completa y comparativa entre diferentes regiones, identificando áreas de mayor potencial energético y posibles barreras de inversión.

1. Boxplot de Irradiación por Región: Un gráfico de caja se empleó para mostrar la variabilidad en la irradiación solar anual en cada región. Esta visualización muestra los valores mínimos, máximos, y los cuartiles de irradiación, destacando tanto la mediana como posibles valores atípicos. Con esta técnica, podemos observar regiones como La Guajira y Cesar, que presentan altos niveles de irradiación solar con variabilidad relativamente baja, lo cual es ideal para instalaciones de energía solar de alta eficiencia. Regiones como Antioquia y Santander, aunque con menor irradiación, muestran una distribución más homogénea que podría favorecer la estabilidad en la generación de energía.
![image](https://github.com/user-attachments/assets/5b6d13df-2d6e-4ce6-8a7b-80985e0a894a)


2. Heatmap de Correlación: Para analizar las relaciones entre variables como irradiación, costo de instalación y energía generada, creamos un mapa de calor que permite identificar patrones de correlación. Este heatmap muestra, por ejemplo, una fuerte correlación entre la irradiación y la energía generada, especialmente en regiones con alta exposición solar. La relación entre el costo de instalación y la energía generada también es significativa en algunas regiones, lo cual es clave para evaluar la rentabilidad de cada sitio de manera integral. La información obtenida con este análisis facilita la identificación de áreas donde el potencial energético justifica mayores inversiones iniciales.
![image](https://github.com/user-attachments/assets/40861de9-6df8-402e-bb8c-a72cd919bf49)


3. Scatterplot con Línea de Regresión: Para evaluar la eficiencia de los costos de instalación en relación con la energía generada, se empleó un gráfico de dispersión con regresión lineal, mostrando la tendencia en cada región. Este análisis ayuda a identificar si el incremento en la inversión de instalación está asociado con un aumento proporcional en la generación de energía. La Guajira y Cesar, por ejemplo, demuestran una relación favorable entre la inversión y la energía generada, lo cual puede guiar decisiones de optimización en términos de rentabilidad.
![image](https://github.com/user-attachments/assets/28795fe0-4380-4303-9125-16884b47a6d6)


## Métodos de Análisis
En términos de técnicas analíticas, implementamos simulaciones de Monte Carlo y análisis de sensibilidad. La simulación de Monte Carlo permitió modelar la variabilidad en la irradiación solar y proyectar diferentes escenarios para la generación de energía en cada región. Realizamos 10,000 iteraciones, lo cual ayudó a identificar la incertidumbre en la generación anual de energía y cómo esta fluctúa debido a variaciones climáticas. Además, el análisis de sensibilidad reveló que el costo de instalación es una variable crucial para determinar la viabilidad del proyecto en cada región, lo que ayuda a enfocar los recursos financieros en las áreas más rentables.

## Resultados Obtenidos
Los resultados preliminares de estos análisis avanzados destacan que La Guajira y Cesar presentan las condiciones ideales para la instalación de sistemas de energía solar, debido a su alta irradiación y favorable relación costo-beneficio. Por otro lado, en regiones como Antioquia y Santander, aunque el potencial de generación es menor, los costos de instalación son competitivos y la variabilidad en irradiación es baja, lo cual podría justificar proyectos con tecnologías menos costosas.

## Conclusión y Próximos Pasos
La implementación de visualizaciones avanzadas y simulaciones ha permitido una comprensión más detallada de la viabilidad de los proyectos de energía solar en cada región. Los próximos pasos incluyen la recopilación de datos reales para validar los resultados ideales proyectados y ajustar el modelo de optimización. Estas mejoras en el modelo permitirán refinar las estrategias de implementación y evaluar de manera precisa la rentabilidad y sostenibilidad a largo plazo de cada proyecto, contribuyendo a un uso más eficiente de los recursos solares en Colombia.

Con esta base sólida, estamos preparados para integrar los datos reales de irradiación y costos específicos en las siguientes etapas, obteniendo así un análisis final que optimice la distribución de recursos en función de la infraestructura y las necesidades de cada región.
