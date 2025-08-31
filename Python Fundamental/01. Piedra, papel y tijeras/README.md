# Juego de Piedra, Papel o Tijeras

Este proyecto es un programa en **Python** que permite jugar al clásico juego de **Piedra, Papel o Tijeras** contra la computadora.  
El juego mantiene un contador de victorias para el jugador y la máquina, mostrando los resultados de cada ronda.

---

## Descripción

El sistema permite al usuario interactuar mediante un menú donde se pueden realizar las siguientes acciones:

- Seleccionar entre Piedra, Papel o Tijeras para jugar contra la computadora.  
- La máquina selecciona su opción de forma aleatoria.  
- Determina el ganador de cada ronda y actualiza un contador de victorias.  
- Muestra los resultados en consola después de cada jugada.  
- Valida entradas incorrectas y notifica errores si el usuario ingresa opciones inválidas.

Este programa sirve como ejemplo práctico para trabajar con **condicionales**, **bucles**, **listas** y manejo básico de entradas en Python.

---

## Ejemplo de uso

1.- Al iniciar el programa, se muestra el menú de opciones:

---------------Juego---------------
1.- Piedra
2.- Papel
3.- Tijeras
Ingrese opción:

2.- Supongamos que el jugador elige "2" (Papel) y la máquina selecciona aleatoriamente "Piedra":

Jugador escoge: Papel
Maquina escoge: Piedra
Papel vs Piedra. Gana Jugador
Contador: Jugador 1 | Maquina 0

3.- Si el usuario ingresa una opción inválida:

Ingrese opción: 5
ERROR: Opción inválida

---

## Resultados esperados

- Cada ronda determina correctamente el ganador según las reglas del juego.  
- Se actualiza un contador acumulativo de victorias del jugador y la máquina.  
- El juego maneja entradas inválidas sin detener la ejecución.  
- Se muestran en consola los resultados de cada ronda de forma clara y comprensible.

---

## Habilidades de Python demostradas

- Uso de **listas** para almacenar opciones y contador de victorias.  
- Aplicación de **condicionales** para determinar el ganador de cada ronda.  
- Implementación de **bucles while** para mantener el juego en ejecución.  
- Uso de **f-strings** para formatear la salida de texto.  
- Manejo de excepciones con "try-except" para entradas inválidas ("ValueError" e "IndexError"). 