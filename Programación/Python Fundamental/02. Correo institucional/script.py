import re

nombre = input("Ingrese el nombre y apellidos: ")

while True:
    if re.match(r"^\D+\s\D+\s\D+$", nombre):
        break
    else:
        nombre = input("ERROR: Ingrese un nombre y dos apellidos: ")

print(f"{nombre[0]}.{nombre.split(' ')[1]}{nombre.split(' ')[2]}@uandresbello.edu")