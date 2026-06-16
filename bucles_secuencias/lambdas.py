
'''las funciones lambda son funciones anonimas paqueñas y de una solo linea que se define usando la palabra clave lambda.'''


# funcion normal

def cuadrado(num):
    return num**2


# misma funcion refactorizada a lambda

def cuadrado_lambda(num): return num ** 2


print(cuadrado_lambda(5))

'''regla general: si la funcion es simple y se usa una sola vez (especialmente como argumento), usa lambda. si es compleja o se reutiliza, usa def'''


# ejemplos

# saber si un numero es par

def es_par(x): return x % 2 == 0


print(es_par(2))

# ejemplo con multiples parametros


def suma(a, b): return a + b


print(suma(10, 5))

# lambdas con condicionales


def prueba(edad): return 'puedes pasar' if edad >= 18 else 'no puedes pasar'

# no se por que el identador convierte las lambda a su sintaxis normal


print(prueba)


# lambdas con map

numeros = [1, 2, 3, 4, 5]

square = list(map(lambda x: x ** 2, numeros))
print(square)
