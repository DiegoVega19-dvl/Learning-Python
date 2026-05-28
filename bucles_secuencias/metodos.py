# para agregar valores nuevos a una lista se usa append

numeros = [1, 2, 3, 4, 5]
numeros.append(6)
print(numeros)


# tambien puedes agregar otras listas

list_numeros = [7, 8, 9, 10]
numeros.append(list_numeros)
print(numeros)
'''se agregan en forma de lista, osea crea una lista anidada, pero si quieres agregar los numeros de esa lista de forma individial debes usar el metodo extend()'''

mas_numeros = [11, 12, 13]
numeros.extend(mas_numeros)
print(numeros)


'''si quieres eliminar un elemento de una lista, puedes usar el elemento remove() toma el valor del elemento a elminar'''

numeros.remove(1)
print(numeros)

'''solo eliminara la primera ocurrencia de un item, no todos los item con el mismo valor'''

'''para eliminar un elemento de un indice especifico puedes usar el elemento pop'''

numeros.pop(0)
print(numeros)

# si no se especifica un elemento, pop eliminara el ultimo

'''para vaciar un lista puede usar el metodo clear()'''

numeros.clear()
print(numeros, 'lista vacia')


''' para ordenar una lista se usa el metodo sort()'''

lista_desordenada = [5, 2, 7, 1, 76, 3]
lista_desordenada.sort()
print(lista_desordenada)
'''esto modifica la lista original, pero si quieres crear un nuevo objeto, puedes usar el metodo sorted()'''

ejemplo = [4, 5, 6, 7, 8]
ejemplo_ordenado = sorted(ejemplo)
