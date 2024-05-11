## Tarea 2:
Realiza la limpieza de los datos “BBDD Alcohol” e indica las inconsistencias encontradas.
Entregables:
1. Sintaxis de consistencia (Puede ser R Studio, Python, Stata o SPSS)
2. Reporte de inconsistencias encontradas

### Resolución:
#### `Sintaxis de consistencia`
- La sintaxis detallada creada para limpiar el DataFrame se encuentra en el archivo notebook [ETL_detallado.ipynb](ETL_detallado.ipynb).
- La sintaxis adaptada a un script de python, para automatizar el trabajo se encuentra en [ETL.py](ETL.py)
- Se recomienda instalar las librerias que se encuentran en el archivo [requirements.txt](requirements.txt), para poder ejecutar correctamente el proceso de limpieza.

#### Reporte de inconsistencias encontradas
- Inicialmente nos encontramos con un DF de 300 registros, el cual al realizar los primeros ``filtros`` del inicio de la encuesta, nos quedamos con unicamente 91 registros para poder analizar posteriormente.
- Encontramos que los datos se han guardado en formato object, int64 y float64. Al revisar el DF encontramos que hay registros con valores ' '(vacios). El problema es que no se estaban guardando correctamente como Nulos. (SOLUCIONADO)
- Se encontró registros que contenian texto y número, procedimos a utilizar una función y quedarnos solo con el número.
- Identifique 18 columnas con todos sus registro nulos, entre ellos las columnas 'P7_4_2', 'P7_4_3', 'P7_5_4', 'NPS_Coderal', etc. Columnas completas en [ETL_detallado.ipynb](ETL_detallado.ipynb).
- Identifique  la cantidad de columnas con más del 50% de registros nulos: 160 columnas
- Se identificó también la cantidad de filas con más del 50% de registro nulos: 87 filas
- Al revisar posibles outliers, no se ha identificado en el DF, lo cual es una buena noticia.