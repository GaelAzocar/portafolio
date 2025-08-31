# Generador de Correo Universitario

Este proyecto es un programa en **Python** que permite generar automáticamente un correo institucional a partir del nombre y los apellidos de un estudiante.  
El correo se crea usando la primera letra del nombre y la combinación de los dos apellidos, siguiendo el formato oficial de la Universidad Andres Bello.

---

## Descripción

El sistema solicita al usuario ingresar **nombre y dos apellidos**, y realiza las siguientes acciones:

- Valida que la entrada contenga exactamente tres palabras usando expresiones regulares ("re").  
- Genera un correo en el formato: "inicial.del_nombre.apellido1apellido2@uandresbello.edu".  
- Imprime el correo resultante en consola para su uso inmediato.

Este programa sirve como ejemplo práctico para trabajar con **regex**, cadenas de texto y manejo básico de entradas en Python.

---

## Ejemplo de uso

1.- Al iniciar el programa, solicita el nombre completo:

Ingrese el nombre y apellidos: Juan Pérez Soto

2.- Generación automática del correo:

j.perezsoto@uandresbello.edu

3.- Validación de entradas incorrectas:

Ingrese el nombre y apellidos: Juan Pérez
ERROR: Ingrese un nombre y dos apellidos: Juan Pérez Soto
j.perezsoto@uandresbello.edu

---

## Resultados esperados

- El programa genera un correo válido para cualquier nombre con **exactamente tres palabras**.  
- Valida que el usuario ingrese **nombre + dos apellidos**.  
- Evita errores al ingresar números u otros caracteres no deseados al inicio o dentro de las palabras.  
- Devuelve el correo en el formato oficial de la universidad de manera consistente.

---

## Habilidades de Python demostradas

- Uso de la librería **re** para validación de patrones de texto.  
- Manejo de cadenas con "split()" y selección de caracteres específicos.  
- Uso de **f-strings** para formatear la salida final del correo.  
- Implementación de un **bucle while** para control de entradas inválidas.  
- Aplicación práctica de **control de flujo y condicionales**.