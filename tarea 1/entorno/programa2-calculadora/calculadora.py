def obtener_numero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print("¡Error! La entrada debe ser un número válido. Intente de nuevo.")

def menu():
    while True:
        print("\n--- CALCULADORA BÁSICA ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '5':
            print("Saliendo de la calculadora...")
            break
            
        if opcion in ['1', '2', '3', '4']:
            num1 = obtener_numero("Ingrese el primer número: ")
            num2 = obtener_numero("Ingrese el segundo número: ")
            
            if opcion == '1':
                print(f"Resultado: {num1 + num2:.17g}")
            elif opcion == '2':
                print(f"Resultado: {num1 - num2:.17g}")
            elif opcion == '3':
                print(f"Resultado: {num1 * num2:.17g}")
            elif opcion == '4':
                if num2 == 0:
                    print("¡Advertencia/Error! No se puede dividir entre cero.")
                else:
                    print(f"Resultado: {num1 / num2:.17g}")
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()