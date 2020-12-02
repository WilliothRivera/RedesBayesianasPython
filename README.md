# README.MD
# Sistema inteligente para la predicción de la secuencia de actividades a partir de un esquema de red bayesiana.

## Características
- En este proyecto se propone usar un modelo probabilístico, particularmente redes bayesianas para capturar dependencia entre los atributos en un registro de eventos para obtener una predicción de la siguiente actividad
- Implementación en lenguaje python.
- Funcionaiento basado en una entrada de bitácora de eventos.


 
## Requerimientos
+ Python 3.x
+ Libreria networkx
+ Librería pyplot from matplotlib
+ Librería csv
+ Librería ascii_uppercase from string

## Entrada de bitácora de eventos
- La entrada de datos inicial consiste en una bitácora de eventos en archivo .txt o .csv, de la siguiente forma:

    Traza1 -> Event1, Event2, Event3, Event4, Event5, EventN... 
	Traza2 -> Event1, Event2, Event4, Event3, Event5, EventN... 
	Traza3 -> Event2, Event4, Event3, Event1, Event5, EventN... 
	
## Procesamiento de bitácoras
- La entrada de datos inicial será transformada de la siguiente forma:

    Traza1 -> A, B, C, D, E, X... 
	Traza2 -> A, B, D, C, E, X... 
	Traza3 -> B, D, C, A, E, X... 

## Procesamiento de trazas
- La secuencia de trazas generada generará de manera automática probabilidades de suceción de eventos.

## Resultado final
- Grafo representativo del flujo de los eventos en cada traza.
- Probabilidades de ocurrencia de actividades dado las anteriores.
- Predicción de eventos.



# Capturas

##### Entrada: 
![](https://1.bp.blogspot.com/-eqjgSPQo6Cg/X8clgu2NdZI/AAAAAAAAHm4/mf7kxLKvNKcIcyQZMVilY-rpV4SqTHrKACLcBGAsYHQ/s1186/entrada.png) 

##### Procesamiento:

![](https://1.bp.blogspot.com/-IMQ5hXWS56A/X8clgARGV4I/AAAAAAAAHmw/241-sZpSU1olVBD5aDBnXrVIHT0AaWPwwCLcBGAsYHQ/s1145/ejecucion.png) 

##### Flujo de eventos:

![](https://1.bp.blogspot.com/-UG-QaOXgyRs/X8clgNKSeLI/AAAAAAAAHms/4JVbK2mkKvUIuQLjMFVofqY52gdMoyrJQCLcBGAsYHQ/s1242/Grafo.png) 

##### Probabilidades:

![](https://1.bp.blogspot.com/-0LX9KIWLTFA/X8clgtChVhI/AAAAAAAAHm0/VTSyOLbQ9RMyUH5APJHKu_UjpUMxIfkJQCLcBGAsYHQ/s1053/probs.png)
