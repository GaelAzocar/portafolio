def calculadora():
    while True:
        a = input("Ingrese A: ")
        b = input("Ingrese B: ")
        c = input("Ingrese C: ")
        try:
            a = int(a)
            b = int(b)
            c = int(c)
            break
        except ValueError:
            print("ERROR: Ingrese un valor válido")
    
    try:
        x1 = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
        x2 = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
        print(f"x1: {round(x1, 2)}, x2: {round(x2, 2)}")
    
    except ZeroDivisionError:
        print("ERROR: Valor A no puede ser 0")
    
    except ValueError:
        print("ERROR: Raíz negativa, no se manejan valores complejos")

calculadora()