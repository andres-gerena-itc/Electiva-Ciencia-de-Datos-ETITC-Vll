# SOLUCIÓN EJERCICIO 3 

Implementar un algoritmo de optimización simple en Python usando el dataset Boston Housing Dataset. Los estudiantes deben:
•	Descargar el dataset desde el enlace proporcionado.
•	Utilizar el algoritmo de gradiente descendente para realizar una regresión lineal.
•	Presentar un informe (400 palabras) explicando la implementación, los resultados y la adecuación del algoritmo para el problema.

## INTRODUCCIÓN

El objetivo de este experimento fue implementar un algoritmo de gradiente descendente para realizar una regresión lineal sobre el California Housing Dataset. Este conjunto de datos contiene información relacionada con características demográficas y socioeconómicas de viviendas en California, lo que permite predecir el valor medio de las casas en diferentes zonas. Utilizando este conjunto de datos, aplicamos el gradiente descendente para ajustar los parámetros de un modelo de regresión lineal y evaluamos su rendimiento a través del error cuadrático medio (MSE).

## METODOLOGÍA
Primero, se cargó y preprocesó el conjunto de datos utilizando fetch_california_housing(). Luego, se dividió en dos conjuntos: entrenamiento (80%) y prueba (20%). Antes de proceder con el algoritmo, fue necesario normalizar las características del conjunto de datos utilizando StandardScaler(), ya que el gradiente descendente se beneficia de características con escalas similares para mejorar la convergencia.

Posteriormente, se implementó el algoritmo de gradiente descendente, comenzando con una inicialización aleatoria de los pesos del modelo (θ). La función de costo utilizada fue el error cuadrático medio (MSE), y se realizó una actualización iterativa de los pesos para minimizar dicho error. Se llevaron a cabo un total de 1000 iteraciones con una tasa de aprendizaje fija de 0.01.
Para evaluar el rendimiento del modelo, se calculó el MSE tanto en el conjunto de entrenamiento como en el conjunto de prueba al final del proceso de entrenamiento. Además, se graficó el comportamiento del MSE en el conjunto de entrenamiento a lo largo de las iteraciones.

## RESULTADOS

Al finalizar el entrenamiento, el modelo alcanzó un MSE de 0.587 en el conjunto de prueba, lo cual indica un error medio moderado en la predicción del valor medio de las viviendas. La gráfica del progreso del MSE mostró una disminución constante del error a medida que aumentaban las iteraciones, lo que sugiere que el algoritmo de gradiente descendente fue efectivo para minimizar la función de costo.
Sin embargo, después de cierto número de iteraciones, el descenso del MSE se estabilizó, lo que indica que el modelo se acercó a una solución óptima dada la tasa de aprendizaje seleccionada. No se observaron signos de divergencia, lo cual sugiere que la tasa de aprendizaje de 0.01 fue adecuada para este problema.

 ![image](https://github.com/user-attachments/assets/df9cf551-0b5d-4c4b-a7d4-e13c735d41b6)


Se agregó una gráfica adicional que en lo personal me parece muy interesante ya que da continuidad y solides a la evaluación de los resultados conforme a la regresión lineal (predicciones vs valores reales).

## PREDICCIONES VS VALORES REALES

En la regresión lineal, una forma fundamental de evaluar el rendimiento del modelo es comparar las predicciones que el modelo hace con los valores reales observados en el conjunto de prueba. Esta comparación ayuda a visualizar cuán bien el modelo está ajustando los datos y si las predicciones están alineadas con los valores reales.

### Implementación de la Gráfica

Para crear esta gráfica, se siguieron estos dos pasos:

1.	Generación de Predicciones: Utilizamos el modelo entrenado para predecir los valores en el conjunto de prueba (X_test_b). Estas predicciones se compararán con los valores reales (y_test).

2.	Creación del Gráfico: La gráfica se crea utilizando un gráfico de dispersión (scatter plot), donde cada punto representa un valor real frente a su predicción correspondiente. La línea diagonal roja en la gráfica actúa como una referencia que indica dónde estarían los puntos si las predicciones coincidieran exactamente con los valores reales.

 ![image](https://github.com/user-attachments/assets/bb538b88-9e98-430f-8dee-8c15978db19e)


## CONCLUSIONES

El experimento demostró la efectividad del gradiente descendente en la optimización de un modelo de regresión lineal para predecir el valor de viviendas. El MSE obtenido muestra un buen ajuste, aunque podría mejorarse ajustando parámetros como la tasa de aprendizaje, el número de iteraciones o empleando técnicas adicionales de regularización. El análisis gráfico también permitió visualizar cómo el algoritmo converge hacia una solución óptima, con una disminución progresiva del error en las iteraciones iniciales.

