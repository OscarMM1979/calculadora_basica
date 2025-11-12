# calculadora.py
# Script básico para operaciones matemáticas
# Autor: OscarMM1979

numero_1 = float(input("Primer número: "))
numero_2 = float(input("Segundo número: "))
operacion = input("Operación (+, -, *, /): ")

if operacion == '+':
    print("Resultado:", numero_1 + numero_2)
elif operacion == '-':
    print("Resultado:", numero_1 - numero_2)
elif operacion == '*':
    print("Resultado:", numero_1 * numero_2)
elif operacion == '/':
    if numero_2 != 0:
        print("Resultado:", numero_1 / numero_2)
    else:
        print("Error: no se puede dividir por cero.")
else:
    print("Operación no válida.")
# calculadora.py
# Versión mejorada

while True:
    numero_1 = float(input("Primer número: "))
    numero_2 = float(input("Segundo número: "))
    operacion = input("Operación (+, -, *, /) o 'q' para salir: ")

    if operacion == 'q':
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break

    if operacion == '+':
        print("Resultado:", round(numero_1 + numero_2, 2))
    elif operacion == '-':
        print("Resultado:", round(numero_1 - numero_2, 2))
    elif operacion == '*':
        print("Resultado:", round(numero_1 * numero_2, 2))
    elif operacion == '/':
        if numero_2 != 0:
            print("Resultado:", round(numero_1 / numero_2, 2))
        else:
            print("Error: no se puede dividir por cero.")
    else:
        print("Operación no válida.")
