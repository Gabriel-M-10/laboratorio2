import operaciones

def menu():
    print("Selecciona una opción:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Exponenciación")
    print("6. Raíz cuadrada")
    print("7. Suma de 5 números")
    print("8. Residuo")
    print("9. Quetzal a Dólar")
    print("10. Dólar a Quetzal")
    print("0. Salir")
import operaciones

def menu():
    print("Selecciona una opción:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Exponenciación")
    print("6. Raíz cuadrada")
    print("7. Suma de 5 números")
    print("8. Residuo")
    print("9. Quetzal a Dólar")
    print("10. Dólar a Quetzal")
    print("0. Salir")

def realizar_operacion(opcion):
    if opcion == 1:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = operaciones.suma(a, b)
        print("El resultado es:", resultado)
    elif opcion == 2:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = operaciones.resta(a, b)
        print("El resultado es:", resultado)
    elif opcion == 3:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = operaciones.multiplicacion(a, b)
        print("El resultado es:", resultado)
    elif opcion == 4:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = operaciones.division(a, b)
        print("El resultado es:", resultado)
    elif opcion == 5:
        a = float(input("Ingrese la base: "))
        b = float(input("Ingrese el exponente: "))
        resultado = operaciones.exponenciacion(a, b)
        print("El resultado es:", resultado)
    elif opcion == 6:
        a = float(input("Ingrese el número: "))
        resultado = operaciones.raiz_cuadrada(a)
        print("El resultado es:", resultado)
    elif opcion == 7:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        c = float(input("Ingrese el tercer número: "))
        d = float(input("Ingrese el cuarto número: "))
        e = float(input("Ingrese el quinto número: "))
        resultado = operaciones.suma_5_numeros(a, b, c, d, e)
        print("El resultado es:", resultado)
    elif opcion == 8:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = operaciones.residuo(a, b)
        print("El resultado es:", resultado)
    elif opcion == 9:
        quetzal = float(input("Ingrese la cantidad en Quetzales: "))
        resultado = operaciones.quetzal_a_dolar(quetzal)
        print("El resultado es:", resultado)
    elif opcion == 10:
        dolar = float(input("Ingrese la cantidad en Dólares: "))
        resultado = operaciones.dolar_a_quetzal(dolar)
        print("El resultado es:", resultado)
    elif opcion == 0:
        print("Saliendo del programa...")
        return False
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")
    
    return True

def main():
    continuar = True

    while continuar:
        menu()
        opcion = int(input("Ingrese una opción: "))
        continuar = realizar_operacion(opcion)

if __name__ == '__main__':
    main()
