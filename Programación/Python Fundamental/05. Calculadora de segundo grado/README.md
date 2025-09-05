# Calculadora de Ecuaciones Cuadráticas

Este proyecto es un programa en **Python** que permite calcular las raíces de ecuaciones cuadráticas de la forma "ax² + bx + c = 0".  
La calculadora trabaja solo con **raíces reales** y notifica al usuario si la ecuación no tiene soluciones reales.

---

## Descripción

El sistema solicita al usuario ingresar los coeficientes "a", "b" y "c" de la ecuación cuadrática y realiza las siguientes acciones:

- Valida que los valores ingresados sean números enteros.  
- Calcula las raíces de la ecuación usando la fórmula general:  
  `x1 = (-b + √(b² - 4ac)) / (2a)`  
  `x2 = (-b - √(b² - 4ac)) / (2a)`  
- Maneja el caso donde "a = 0" y notifica al usuario que no es posible dividir por cero.  
- Notifica si la ecuación no tiene raíces reales (cuando el discriminante es negativo).  

Este programa sirve como ejemplo práctico para trabajar con **condicionales**, **bucles**, **manejo de excepciones** y **f-strings** en Python.

---

## Ejemplo de uso

1.- Al iniciar el programa, solicita los coeficientes de la ecuación:

Ingrese A: 1
Ingrese B: -3
Ingrese C: 2

2.- Cálculo de las raíces:

x1: 2.0, x2: 1.0

3.- Si se ingresa "A = 0":

Ingrese A: 0
Ingrese B: 2
Ingrese C: 1
ERROR: Valor A no puede ser 0

4.- Si el discriminante es negativo:

Ingrese A: 1
Ingrese B: 2
Ingrese C: 5
ERROR: Raíz negativa, no se manejan valores complejos

---

## Resultados esperados

- El programa calcula correctamente las raíces reales de ecuaciones cuadráticas.  
- Maneja errores de división por cero cuando "a = 0".  
- Notifica al usuario cuando la ecuación no tiene raíces reales.  
- Solicita repetidamente la entrada hasta que los coeficientes sean válidos.  

---

## Habilidades de Python demostradas

- Uso de **bucles while** para validación de entradas.  
- Manejo de **try-except** para capturar errores de tipo y división por cero.  
- Uso de **f-strings** para mostrar resultados formateados.  
- Aplicación de **condicionales** para controlar casos especiales (discriminante negativo, "a = 0").  
- Validación de datos ingresados por el usuario antes de realizar cálculos.