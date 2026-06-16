'''una de las principales ventajas de python es que una misma funcionalidad puede ser escrita de maneras muy diferentes, ya que su sintaxis es muy rica en lo que se conoce como expresiones idiomaticas o idiomatic expressions. las list comprhesion o compresion de listas son una de ellas'''


'''las list comprehesion nos permite crear listas de elementos en una sola linea de codigo.'''

# ejemplo de compresion de listas

cuadrado = [i**2 for i in range(5)]
print(cuadrado)


# sin compresion de listas

cuadrados = []

for i in range(5):
    cuadrados.append(i**2)

print(cuadrados)


'''la expresion tambien puedes ser una llamada a una funcion. se podria escribir el ejemplo anterior del calculo de cuadrados de la siguiente manera'''


def elevado_cuadrado(i):
    return i**2


resultado = [elevado_cuadrado(i) for i in range(5)]

print(resultado)


'''cualquier elemento que sea iterable puede ser usado con las list comprehesions'''


# ejemplo usando if else

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
resultado = [(num, 'Par') if num % 2 == 0 else (num, 'Impar')
             for num in numeros]
print(resultado)


# funcion filter

numeros_pares = filter(lambda n: n % 2 == 0, numeros)
print(list(numeros_pares))


'''la funcion map en python, toma un iterable y aplica una funcion a cada uno de sus elementos '''


centigrados = [23, 45, 100, 50, 80]


def to_fahrenheit(grados):
    return (grados * 9/5) + 32


fahrenheit = list(map(to_fahrenheit, centigrados))
print(fahrenheit)
