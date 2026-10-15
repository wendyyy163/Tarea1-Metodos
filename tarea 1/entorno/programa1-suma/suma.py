import sys

if len(sys.argv) >= 3:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
else:
    try:
        x = float(input("Ingrese el numero 1: "))
    except ValueError:
        x = 0.1
    try:
        y = float(input("Ingrese el numero 2: "))
    except ValueError:
        y = 0.2

resultado = x + y
print(f"{resultado:.17g}")