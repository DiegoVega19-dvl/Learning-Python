from collections.abc import Iterable

# FOR LOOP

for i in range(0, 5):
    print(i)


# en python puedes iterar cadenas

for i in "hola mundo":
    print(i)


"""todo lo que va despues del 'in' debe ser un iterable
siempre debe ser un iterable, si no el programa te marcara un error"""

# Lista
for x in [1, 2, 3]:
    print(x)

# String
for letra in "hola":
    print(letra)

# Tupla
for item in (10, 20):
    print(item)

# Diccionario (itera por claves)
for clave in {"a": 1, "b": 2}:
    print(clave)

# Conjunto
for valor in {1, 2, 3}:
    print(valor)

# range también es iterable
for i in range(5):
    print(i)



# como saber si un objeto o variable es iterable
# con el metodo 'Iterable'
numero = 50
lista = [10, 15, 20]
cadena = "una cadena"

print(isinstance(numero, Iterable))
print(isinstance(lista, Iterable))
print(isinstance(cadena, Iterable))
