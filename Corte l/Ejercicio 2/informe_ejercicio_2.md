# SOLUCIÓN EJERCICIO 2 

Usar un conjunto de datos común y accesible para realizar un análisis descriptivo. 
Los estudiantes deben:

1.	Descargar el dataset. 
2.	Utilizar Python con Pandas y NumPy para calcular estadísticas descriptivas (media, mediana, desviación estándar).
3.	Crear un breve informe (400 palabras) con los resultados obtenidos y una interpretación de estos.


## INTRODUCCIÓN

El análisis realizado sobre el conjunto de datos California Housing se enfoca en entender las características demográficas y geográficas de las viviendas en California, prestando especial atención a las estadísticas descriptivas de las variables. Este informe explora aspectos como la media, mediana, desviación estándar, y la distribución de la variable objetivo, MEDV (precio medio de las viviendas), y las variables explicativas.

## Descripción general del conjunto de datos

El conjunto de datos cuenta con ocho variables independientes y una variable objetivo (MEDV), que representa el precio medio de las viviendas. Las variables independientes incluyen características como el ingreso medio de la zona (MedInc), la antigüedad de la vivienda (HouseAge), el número promedio de habitaciones (AveRooms), el número promedio de dormitorios (AveBedrms), la población, la ocupación promedio (AveOccup), la latitud y la longitud.

## Análisis estadístico descriptivo 

### 1.	Media, mediana y desviación estándar:

MEDV (precio medio de las viviendas) tiene una media de 2.07 ($20,685), una mediana de 1.80 ($17,970) y una desviación estándar de 1.15. Esto indica que los precios de las viviendas tienden a concentrarse alrededor de los $20,000, pero con una dispersión notable, lo que sugiere la existencia de viviendas con precios muy por encima o por debajo del promedio. (página 5, Tabla #3)

MedInc (ingreso medio de la zona) muestra una media de 3.87, es decir, $38,700, con una desviación estándar de 1.90. La mediana es de 3.53, lo que indica que el 50% de las zonas tienen un ingreso medio menor o igual a $35,348.


HouseAge (edad promedio de las viviendas) tiene una media de 28.64 años, lo que refleja que la mayoría de las viviendas tienen más de dos décadas de antigüedad. La desviación estándar de 12.59 sugiere una distribución de viviendas de diferentes épocas.

### 2.	Rango y dispersión de variables:

MedInc oscila entre 0.50 y 15.00, lo que muestra una gran variación en los niveles de ingresos medios de las zonas. Este amplio rango refleja la diversidad socioeconómica en California.

AveRooms (promedio de habitaciones por vivienda) tiene una media de 5.43, pero su rango va desde 0.85 hasta 141.91. Este rango extremo sugiere que algunas viviendas tienen configuraciones atípicas en cuanto al número de habitaciones.

Population tiene un rango bastante amplio, desde 3 hasta 35,682 habitantes por zona, lo que resalta la variabilidad en densidad poblacional.

## Distribución de precios: 
El histograma de la variable MEDV muestra una distribución asimétrica, con la mayoría de los precios concentrados en los rangos más bajos. Esto sugiere que la mayoría de las viviendas tienen precios relativamente bajos o moderados, con algunas excepciones que representan viviendas significativamente más caras.

 ![image](https://github.com/user-attachments/assets/f025a4b5-55d3-463c-87e2-9da7a6cec95f)


## Tablas obtenidas desde Python:

### Tabla #1:

![image](https://github.com/user-attachments/assets/f52421b1-6a2a-4f52-b081-af6d99f1fdcb)

### Tabla #2:

 ![image](https://github.com/user-attachments/assets/2eb19c0e-c679-45a0-954c-0cf562b5303f)


### Tabla #3: Media, Mediana y Desviación estándar
 
![image](https://github.com/user-attachments/assets/a260e6bd-cb6a-4f28-9b68-4fdff1fa1b5b)

![image](https://github.com/user-attachments/assets/17054e17-07db-4f6a-9f9b-63338f819efd)


## CONCLUSIÓN

Los resultados de las estadísticas descriptivas indican que existe una gran variabilidad en las características socioeconómicas y demográficas de las viviendas en California. El ingreso medio de las zonas tiene un impacto considerable en los precios de las viviendas, mientras que otras variables como el número promedio de habitaciones y la población muestran rangos muy amplios, sugiriendo configuraciones diversas. El análisis estadístico proporciona una comprensión general del mercado inmobiliario en California, destacando la heterogeneidad en los precios y las características de las viviendas.


## DETALLES TÉCNICOS EJERCICIO 2

Se utilizó Jupyter junto con las importaciones requeridas para la preparación del entorno y correcta extracción de los datos requeridos

1. Importación de librerías
   
Primero, se importan las librerías necesarias para el análisis:
•	Pandas y Numpy: Para manejar los datos y realizar cálculos numéricos.
•	Matplotlib y Seaborn: Para visualizar los datos mediante gráficos.
•	Scikit-learn: Para dividir el conjunto de datos y aplicar un modelo de regresión lineal.

2. Carga del conjunto de datos
   
Se carga el conjunto de datos de California Housing utilizando la función fetch_california_housing() de Scikit-learn. Este conjunto contiene información sobre características de viviendas y su precio en diferentes áreas de California.

3. Conversión a DataFrame
   
Se convierte el conjunto de datos en un DataFrame de Pandas para facilitar su manejo. Luego, se añade una columna nueva llamada MEDV que contiene los precios medios de las viviendas.

4. Exploración inicial de los datos
   
Se visualizan las primeras filas del DataFrame con df.head() y se generan estadísticas básicas con df.describe() para entender la estructura y las características generales del conjunto de datos.

5. Cálculo de estadísticas descriptivas
   
Se calculan tres estadísticas importantes para la columna MEDV (precio medio de las viviendas):
•	Media: El precio medio de todas las viviendas.
•	Mediana: El valor que divide al conjunto de precios en dos partes iguales.
•	Desviación estándar: Mide cuánto varían los precios con respecto a la media.

6. Visualización de la distribución de precios
   
Se genera un histograma para visualizar cómo están distribuidos los precios de las viviendas. Esto ayuda a ver si los precios se concentran en ciertos rangos o si están muy dispersos.


7. Matriz de correlación
   
Se calcula una matriz de correlación para observar cómo se relacionan las diferentes variables del conjunto de datos entre sí. Luego, se visualiza esta matriz con un gráfico de calor (heatmap) para identificar rápidamente qué variables tienen una relación más fuerte con el precio de las viviendas.

8. División del conjunto de datos
   
El conjunto de datos se divide en dos partes:
•	Conjunto de entrenamiento: El 80% de los datos, que se usarán para entrenar el modelo.
•	Conjunto de prueba: El 20% restante, que se usará para probar qué tan bien predice el modelo.

9. Entrenamiento del modelo
    
Se entrena un modelo de regresión lineal con los datos de entrenamiento. La regresión lineal trata de encontrar una relación entre las variables explicativas (por ejemplo, ingreso medio, número de habitaciones) y el precio medio de las viviendas.

10. Predicción y evaluación
    
Una vez entrenado, el modelo se usa para predecir los precios en el conjunto de prueba. Finalmente, se calcula el error cuadrático medio (MSE), que mide qué tan lejos están las predicciones del modelo de los valores reales. Un valor de error bajo significa que el modelo predice bien.
