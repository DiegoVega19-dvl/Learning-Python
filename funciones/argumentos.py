def parametros_indeterminados(*args):
    print(*args)


# parametros_indeterminados(5, "hola mundo", [1, 2, 3])

# argumentos clave : valor


def indeterminado_nombre(**kwargs):
    print(kwargs)


# indeterminado_nombre(n=5, c="hola", d=[1, 2, 3])

# funcion suma con n argumentos


def suma_indefinida(*args):
    s = 0
    for arg in args:
        s += arg
    return s


print(suma_indefinida(1, 2, 2, 3, 4))


def paises(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])


# paises(mexico="mexico", argentina="argentina", españa="españa")
