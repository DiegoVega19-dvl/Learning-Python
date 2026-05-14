"""def dividir(a, b):
    try:
        return a/b
    except:
        print("no se puede dividir entre cero")


print(dividir(20, 0)) """

"""while (True):
    try:
        n = int(input("introduce un numero: "))
        m = int(input("introduce otro numero: "))
        print(n/m)
        break
    except Exception as e:
        print(type(e).__name__)"""


# invocacion de excepciones

"""def funcion(algo=None):
    if algo is None:
        raise ValueError("Error no se permiten valores nulos")
    


funcion()"""


# ejercicio 1: divison entre 0

def division(a, b):
    try:
        return a/b
    except Exception as e:
        print(type(e).__name__)


print(division(100, 10))

# ejercicio 2: indice

lista = [1, 2, 3, 4, 5]

try:
    lista[10]
except IndexError:
    print("el indice que quieres acceder no existe dentro de la lista")


# ejercicio 3: diccionario de datos

colores = {'azul': 'blue', 'rojo': 'red', 'verde': 'green'}

try:
    colores['cafe']
except KeyError:
    print("el color que quieres acceder no existe")


# ejercicio 4: type error

try:
    resultado = "15" + 20
except TypeError:
    print("solo se pueden sumar numeros del mismo tipo osea... enteros")


# ejercicio 5: elementos de la lista

ele = [0, 10, -2]


def agregar(lista, elemento):
    try:
        if elemento in lista:
            raise ValueError
        else:
            lista.append(elemento)
    except ValueError:
        print("no puede agregar numero duplicados => {}".format(elemento))


print(agregar(ele, 5))
print(ele)
