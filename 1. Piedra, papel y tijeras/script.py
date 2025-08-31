import random

opciones = ["Piedra", "Papel", "Tijeras"]
contador = [0, 0]

def juego(jugador, maquina):
    print(f"\nJugador escoge: {jugador}\nMaquina escoge: {maquina}")
    
    if (jugador == "Papel" and maquina == "Piedra") or \
       (jugador == "Piedra" and maquina == "Tijeras") or \
       (jugador == "Tijeras" and maquina == "Papel"):
        print(f"{jugador} vs {maquina}. Gana Jugador")
        contador[0] += 1
        
    elif (maquina == "Papel" and jugador == "Piedra") or \
         (maquina == "Piedra" and jugador == "Tijeras") or \
         (maquina == "Tijeras" and jugador == "Papel"):
        print(f"{maquina} vs {jugador}. Gana Maquina")
        contador[1] += 1
    
    else:
        print(f"{jugador} vs {maquina}. Empate")
    
    print(f"Contador: Jugador {contador[0]} | Maquina {contador[1]}")

while True:
    print("-" * 15 + "Juego" + "-" * 15)
    ingreso = input("1.- Piedra\n2.- Papel\n3.- Tijeras\nIngrese opción: ")
    opcion_maquina = random.choice(opciones)
    
    try:
        opcion_jugador = opciones[int(ingreso) - 1]
        juego(opcion_jugador, opcion_maquina)
    except (ValueError, IndexError):
        print("ERROR: Opción inválida")
