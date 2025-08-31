from collections import Counter
import pandas as pd
import os

def cargar_resultados():
    global datos
    nombre = input("Nombre del archivo con extensión: ").strip()
    if os.path.exists(nombre):
        with open(nombre) as archivo:
            datos = archivo.read().replace("\n", "").strip()
    else:
        print(f"ERROR: No existe el archivo {nombre}")

def mostrar_resultados():
    global si, no, nulo
    conteo = Counter(datos)
    si = int(conteo.get("1", 0))
    no = int(conteo.get("0", 0))
    nulo = int(conteo.get("2", 0))
    
    print(f"Sí: {si} // {si * '*'}")
    print(f"No: {no} // {no * '*'}")
    print(f"Nulo: {nulo} // {nulo * '*'}")

def mostrar_porcentajes():
    total = si + no + nulo
    if total == 0:
        print("ERROR: No hay datos para calcular porcentajes")
        return
    print(f"Sí: {si / total * 100:.2f}%")
    print(f"No: {no / total * 100:.2f}%")
    print(f"Nulo: {nulo / total * 100:.2f}%")

def exportar_resultados():
    nombre = input("Nombre del archivo sin la extensión: ").strip()
    df = pd.DataFrame({"Sí": [si], "No": [no], "Nulo": [nulo]})
    df.to_csv(f"{nombre}.csv", index=False)
    print(f"Archivo '{nombre}.csv' exportado correctamente.")

def menu():
    print("-"*15 + " Menú principal " + "-"*15)
    opcion = input(
        "1. Cargar resultados\n"
        "2. Mostrar resultados\n"
        "3. Mostrar porcentajes\n"
        "4. Exportar resultados\n"
        "5. Salir\n"
        "Ingrese opción: "
    ).strip()
    
    if opcion == "1":
        cargar_resultados()
    elif opcion == "2":
        mostrar_resultados()
    elif opcion == "3":
        mostrar_porcentajes()
    elif opcion == "4":
        exportar_resultados()
    elif opcion == "5":
        exit()
    else:
        print("ERROR: Opción inválida")

while True:
    try:
        menu()
    except NameError:
        print("ERROR: El archivo no ha sido cargado")
