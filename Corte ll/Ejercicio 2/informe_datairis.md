URL CÓDIGO PYTHON EN GOOGLE COLAB: https://colab.research.google.com/drive/12B_SzLDJvLwAJL7p-1IDHqb_f8trvyW4?usp=sharing

# INFORME DE VISUALIZACIÓN DATASET IRIS

El dataset Iris es uno de los conjuntos de datos más utilizados para el análisis de clasificación. Consta de tres especies de iris: setosa, versicolor y virginica, y cuatro características para cada observación: longitud y ancho del sépalo, y longitud y ancho del pétalo. Utilizando Google Colab, se emplearon las bibliotecas de visualización de datos Matplotlib y Seaborn para representar este conjunto de datos en gráficos que faciliten el análisis de sus patrones y relaciones.

## 1. Gráficos de Dispersión y Distribución
El primer gráfico es un gráfico de dispersión que muestra la relación entre la longitud y el ancho del sépalo. Esta representación permite observar cómo estas dos características varían según cada espécimen, revelando patrones importantes en cuanto a la separación entre especies. Se puede ver que la especie setosa tiende a agruparse en un área específica, lo cual sugiere que estas variables pueden ayudar en la clasificación de esta especie en particular.
Para comprender la distribución de una sola variable, se creó un histograma para la longitud del pétalo. Este gráfico revela que la mayoría de los especímenes tienen pétalos de longitud menor a 2 cm o entre 4 y 6 cm, destacando una distribución bimodal. Este patrón sugiere la existencia de dos grupos distintos en el dataset, alineados con las especies de iris.

![image](https://github.com/user-attachments/assets/e9712ae6-f1d4-45f1-af1f-4fe0890bbf89)

Imagen 1: Grafico Dispersión

## 2. Gráfico de Pares (Pairplot)
El gráfico de pares, generado con Seaborn, permite una visión más completa de las relaciones entre las cuatro variables en pares de gráficos de dispersión. Al colorear cada punto según la especie, se observa que setosa es claramente diferenciable de las otras dos especies, mientras que versicolor y virginica presentan mayor superposición. Este gráfico de pares facilita la identificación de características útiles para clasificar las especies, mostrando que la longitud y ancho del pétalo son variables con mayor poder discriminatorio.

![image](https://github.com/user-attachments/assets/b65f303e-97c4-4b1b-8c10-9e6287371d40)

Imagen 2: Grafico Pares



## 3. Mapa de Calor de la Correlación
El mapa de calor de la matriz de correlación de las variables numéricas permite evaluar la fuerza de las relaciones entre ellas. Este gráfico destaca una alta correlación positiva entre la longitud y el ancho del pétalo, lo que implica que, a mayor longitud de pétalo, también aumenta su ancho. Sin embargo, entre la longitud y el ancho del sépalo, la correlación es mucho más baja, sugiriendo que estas variables pueden aportar información complementaria en lugar de redundante.

![image](https://github.com/user-attachments/assets/345f3be9-792f-4219-98d2-e5b3b17d4b9f)

Imagen 3: Grafico Mapa de Calor de Correlación

## Conclusiones
La visualización de datos del dataset Iris demuestra la efectividad de gráficos de dispersión, histogramas, gráficos de pares y mapas de calor en el análisis de datos. Los gráficos revelan patrones y correlaciones que ayudan en la comprensión de las relaciones entre las variables, y muestran cómo algunas características específicas, como las dimensiones del pétalo, son útiles para diferenciar entre especies. Este análisis preliminar sugiere que las técnicas de visualización son esenciales en la exploración de datos y en la identificación de relaciones que pueden ser utilizadas en modelos de clasificación.

