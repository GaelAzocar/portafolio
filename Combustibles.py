import pandas as pd
import matplotlib.pyplot as plt

estanques = ["Estanque 1", "Estanque 2", "Estanque 3", "Estanque 4", "Estanque 5"]
cargas = [0, 0, 0, 0, 0]
valor = [0, 0, 0, 0, 0]

def color():
    colores = []
    for estanque in cargas:
        if estanque < 2000:
            colores.append("red")
        elif 2000 <= estanque < 6000:
            colores.append("yellow")
        else:
            colores.append("green")
    return colores

def mostrar_combustible():
    print("-" * 10 + " Información " + "-" * 10)
    print(df.to_string(index=False))
    print("Verde: Alto, Amarillo: Medio, Rojo: Bajo\n")
    plt.bar(estanques, cargas, color=color())
    plt.ylabel("Combustible (Litros)")
    plt.title("Estanques")
    plt.show()

def cargar_combustible():
    print("-" * 10 + " Carga de combustible " + "-" * 10)
    print(df[["Estanques", "Combustible"]].to_string(index=False))
    seleccion_estanque = int(input("Seleccione estanque (1,2,3,4,5): "))

    while True:
        cargar_estanque = int(input("Ingrese cuánto combustible quiere cargar: "))
        if cargas[seleccion_estanque-1] + cargar_estanque > 10000:
            print("ERROR: Capacidad máxima alcanzada")
        else:
            break

    cargas[seleccion_estanque-1] += cargar_estanque
    print(f"La carga del estanque {seleccion_estanque} con {cargar_estanque} litros ha sido realizada.\n")

def descargar_combustible():
    print("-" * 10 + " Descarga de combustible " + "-" * 10)
    print(df[["Estanques", "Combustible"]].to_string(index=False))
    seleccion_estanque = int(input("Seleccione estanque (1,2,3,4,5): "))

    while True:
        descarga_estanque = int(input("Ingrese cuánto combustible quiere descargar: "))
        if cargas[seleccion_estanque-1] - descarga_estanque < 0:
            print("ERROR: No puede descargar más de lo que contiene el estanque")
        else:
            break

    cargas[seleccion_estanque-1] -= descarga_estanque
    print(f"La descarga del estanque {seleccion_estanque} con {descarga_estanque} litros ha sido realizada.\n")

def transferencia_combustible():
    print("-" * 10 + " Transferencia de combustible " + "-" * 10)
    print(df[["Estanques", "Combustible"]].to_string(index=False))
    primer_estanque = int(input("Seleccione el primer estanque (1,2,3,4,5): "))

    while True:
        carga = int(input("Ingrese cuánto combustible quiere transferir: "))
        if cargas[primer_estanque-1] - carga < 0:
            print("ERROR: No puede transferir más de lo que contiene el estanque")
        else:
            while True:
                segundo_estanque = int(input("Ingrese el segundo estanque (1,2,3,4,5): "))
                if cargas[segundo_estanque-1] + carga > 10000:
                    print("ERROR: Capacidad máxima alcanzada, seleccione otro estanque")
                else:
                    break
            break

    cargas[primer_estanque-1] -= carga
    cargas[segundo_estanque-1] += carga
    print(f"La transferencia de {carga} litros del estanque {primer_estanque} al estanque {segundo_estanque} ha sido realizada.\n")

def ajustar_precio():
    print("-" * 10 + " Ajuste de precios " + "-" * 10)
    print(df[["Estanques", "Valor"]].to_string(index=False))
    ajuste = int(input("Ingrese el número del estanque cuyo precio desea cambiar (1,2,3,4,5): "))
    nuevo_valor = int(input("Ingrese el nuevo valor: "))
    valor[ajuste-1] = nuevo_valor
    print(f"El valor del estanque {ajuste} ha sido actualizado a ${nuevo_valor}.\n")

def menu():
    print("-" * 15 + " Menú principal " + "-" * 15)
    print("1. Mostrar combustible\n2. Cargar combustible\n3. Descargar combustible\n4. Transferir combustible\n5. Ajustar precio\n6. Salir")

    opcion = input("Ingrese opción: ")
    if opcion == "1":
        mostrar_combustible()
    elif opcion == "2":
        cargar_combustible()
    elif opcion == "3":
        descargar_combustible()
    elif opcion == "4":
        transferencia_combustible()
    elif opcion == "5":
        ajustar_precio()
    elif opcion == "6":
        exit()
    else:
        print("ERROR: Opción inválida")

while True:
    try:
        df = pd.DataFrame({"Estanques": estanques, "Combustible": cargas, "Valor": valor})
        menu()
    except ValueError:
        print("ERROR: Verifique los datos ingresados")
    except IndexError:
        print("ERROR: No se ha seleccionado un estanque válido")