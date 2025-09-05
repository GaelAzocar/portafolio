# Análisis de Resultados de Votación

Este proyecto es un programa en **Python** que permite cargar, analizar y exportar los resultados de una votación simple.  
El programa muestra la cantidad de votos a favor ("Sí"), en contra ("No") y nulos, incluyendo representación gráfica con asteriscos y porcentajes.

---

## Descripción

El sistema permite al usuario interactuar mediante un menú donde se pueden realizar las siguientes acciones:

- Cargar un archivo de texto con los resultados de la votación (valores "1" para Sí, "0" para No, "2" para Nulo).  
- Mostrar los resultados totales y representar cada categoría con asteriscos en consola.  
- Calcular y mostrar los porcentajes de cada categoría sobre el total de votos.  
- Exportar los resultados a un archivo CSV.  
- Validar que el archivo exista y que los datos estén cargados antes de realizar cálculos.

Este programa sirve como ejemplo práctico para trabajar con **colecciones**, **manejo de archivos**, **listas**, **diccionarios**, **bucles**, **f-strings** y manejo básico de errores en Python.

---

## Ejemplo de uso

1.- Al iniciar el programa, se muestra el menú principal:

--------------- Menú principal ---------------

1. Cargar resultados
2. Mostrar resultados
3. Mostrar porcentajes
4. Exportar resultados
5. Salir
Ingrese opción:

2.- Supongamos que el usuario carga un archivo llamado "votos.txt" con los valores:

1
0
1
2
1

3.- Mostrar resultados en consola:

Sí: 3 // ***
No: 1 // *
Nulo: 1 // *

4.- Mostrar porcentajes:

Sí: 60.00%
No: 20.00%
Nulo: 20.00%

5.- Exportar resultados a CSV:

Nombre del archivo sin la extensión: resultados_votacion
Archivo "resultados_votacion.csv" exportado correctamente.

6.- Si el usuario intenta mostrar resultados sin cargar el archivo:

ERROR: El archivo no ha sido cargado

---

## Resultados esperados

- Conteo correcto de votos para Sí, No y Nulo.  
- Representación visual en consola con asteriscos proporcional a cada categoría.  
- Cálculo correcto de porcentajes incluso si hay cero votos.  
- Exportación de resultados a CSV funcionando correctamente.  
- Manejo de entradas y archivos inexistentes sin detener la ejecución del programa.

---

## Habilidades de Python demostradas

- Uso de **Counter** para contar elementos en una lista o cadena.  
- Manejo de **archivos** para leer y escribir información.  
- Uso de **listas y variables globales** para almacenar resultados.  
- Implementación de **bucles while** para mantener el menú en ejecución.  
- Uso de **f-strings** para formatear la salida de resultados y porcentajes.  
- Manejo de excepciones con **try-except** para validar archivos cargados.