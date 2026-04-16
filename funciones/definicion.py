def saludar():
    print("hola mundo, esto es una funcion")


# saludar()


def tabla_del_5():
    for i in range(11):
        print("5 * ", i, " = ", i*5)


# tabla_del_5()


def suma(a, b):
    return a + b


print(suma(15, 12))

# funcion de es par o impar


def isEven(a):
    if a % 2 == 0:
        print("is Even")
    else:
        print("is Odd")


isEven(15)

# resta


def resta(a, b):
    return a - b


print(resta(100, 25))
