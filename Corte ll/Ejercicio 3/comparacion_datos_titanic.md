URL CÓDIGO PYTHON EN GOOGLE COLAB EJERCICIO 3: https://colab.research.google.com/drive/15Tip2uxn0xSmLlFnzKveioRqix2aXo7C?usp=sharing

# COMPARACIÓN DE DATOS DATASET TITANIC

En el análisis comparativo de Ciencia de Datos y Big Data, es fundamental entender cómo estas áreas afectan las técnicas de visualización, especialmente en relación con las visualizaciones empleadas en el ejercicio con el dataset de Titanic.

En el caso de la Ciencia de Datos, se aplicaron visualizaciones detalladas como el gráfico de barras para mostrar la supervivencia por clase y el histograma para la distribución de edad según supervivencia. Estas visualizaciones se realizaron con Matplotlib y Seaborn, herramientas que permiten un enfoque exploratorio. La técnica de visualización en estos casos facilita un análisis profundo y personalizado; por ejemplo, los gráficos de barras permiten observar las diferencias entre clases y la relación con la supervivencia, mientras que el histograma muestra tendencias en la edad de los pasajeros según su supervivencia. Estas técnicas no solo son intuitivas y fáciles de interpretar, sino que también ofrecen detalles granulares útiles para comprender la estructura y patrones dentro de un dataset de tamaño moderado.

![image](https://github.com/user-attachments/assets/defe53f0-6745-413d-968e-59ee9a66d1bc)

Imagen 1: Supervivencia por clase

![image](https://github.com/user-attachments/assets/331e6e49-0fdf-4e17-8e5c-4639baf98723)

Imagen 2: Distribución según supervivencia

En cambio, en el contexto de Big Data, trabajar con un dataset masivo como el de Titanic requeriría visualizaciones escalables. Una técnica simulada en el ejercicio fue el procesamiento en lotes, que mostró cómo las visualizaciones de edad por supervivencia podrían dividirse en grupos más pequeños para su análisis. Sin embargo, en un entorno real de Big Data, las visualizaciones requieren herramientas como Apache Spark o Plotly, que gestionan grandes volúmenes de datos y ofrecen interactividad en gráficos de líneas, mapas de calor simplificados o paneles de control en tiempo real. Estas técnicas buscan detectar patrones globales rápidamente y no profundizan en detalles específicos de cada subgrupo, como sí lo hace el análisis en Ciencia de Datos.

![image](https://github.com/user-attachments/assets/dcc11ada-a63f-4c4f-b49c-f950471fe987)

![image](https://github.com/user-attachments/assets/8c5620c8-d776-46fe-bc5e-283c0b3d2860)

![image](https://github.com/user-attachments/assets/b302ecf1-bf9b-49c1-afb5-e644e0ac46a3)

![image](https://github.com/user-attachments/assets/858b9105-92a3-4c9d-aa14-e6bb44437b7a)

Imagenes de visualizaciones escalables en lote (BATCH)

Así, las técnicas de visualización en Ciencia de Datos se enfocan en el análisis exploratorio detallado, mientras que en Big Data se prioriza la rapidez y la escalabilidad, optimizando las visualizaciones para obtener conclusiones generales y responder eficientemente en tiempo real.
