import math


# ejercicio 1

def area_rectangulo(base, altura):
    area = base * altura
    return f"el area del rectangulo es: {area}"


# print(area_rectangulo(15, 10))

# ejercicio 2


def area_circulo(r):
    area = math.pi * r * r
    return f"el area del circulo es: {area}"


# print(area_circulo(5))


# ejercicio 3

def relacion(num1, num2):
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0


# print(relacion(5, 5))


# ejercicio 4

def intermedio(a, b):
    return (a + b)/2


# print(intermedio(-12, 24))


# ejercicio 5

def recortar(numero, inferior, superior):
    if numero < inferior:
        return inferior
    elif numero > superior:
        return superior
    else:
        return numero


# print(recortar(15, 0, 10))


# ejercicio 6

def separar(lista):
    lista.sort()
    pares = []
    impares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares


pares, impares = separar([2, 3, 5, 1, 4, 66, 44, 12])

print(pares)
print(impares)
