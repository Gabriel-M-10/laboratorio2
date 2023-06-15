import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero."
    
def exponenciacion(a, b):
    return a ** b

def raiz_cuadrada(a):
    return math.sqrt(a)

def suma_5_numeros(a, b, c, d, e):
    return a + b + c + d + e

def residuo(a, b):
    return a % b