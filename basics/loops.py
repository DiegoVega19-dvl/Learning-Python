from collections.abc import Iterable

# FOR LOOP

for i in range(0, 5):
    print(i)


# en python puedes iterar cadenas

for i in "hola mundo":
    print(i)


"""todo lo que va despues del 'in' debe ser un iterable,
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


# WHILE LOOP


# esto generara un loop infinito, mientras 10 siga siendo menor que 20
while 10 < 20:
    print("esto es un loop")
    break  # la palabra reservada 'break' sirve para romper esos loops infinitos


n1 = 10
while n1 <= 100:
    print("hola mundo esto es un loop")
    n1 += 10
if n1 >= 100:
    print("loop finalizado")
else:
    print("ocurrio un error")


paises = ["mexico", "argentina", "brazil"]
for index, pais in enumerate(paises):
    print(index, "-->>", pais)


number = 5
while number != 0:
    print(number)
    number -= 1


teams = {
    "Colorado": "Rockies",
    "Chicago": "White Sox",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
}

for key, team in teams.items():
    print(key, "--->", team)


# como saber si un objeto o variable es iterable
# con el metodo 'Iterable'
numero = 50
lista = [10, 15, 20]
cadena = "una cadena"

print(isinstance(numero, Iterable))
print(isinstance(lista, Iterable))
print(isinstance(cadena, Iterable))
