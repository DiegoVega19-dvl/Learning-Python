
# cuenta regresiva

def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)  # aqui la funcion se llama a si misma
    else:
        print("se termino la cuenta")


# print(cuenta_regresiva(10))

# factorial


def factorial(num):
    if num > 1:
        num = num * factorial(num - 1)
        print("hola")
    return num


# print(factorial(5))


# sumatoria
def sumatoria(numero):
    if numero > 1:
        numero = numero + sumatoria(numero - 1)
    return numero


print(sumatoria(5))
