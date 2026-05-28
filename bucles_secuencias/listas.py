# si quieres saber si un elemento se encuentra en la lista
# puedes usar la plabra in

frutas = ['sandia', 'datil', 'mango']
print('sandia' in frutas)


# listas anidadas

'''en este ejemplo para acceder a los elementos de la lista anidada
debes poner un segundo indice, igual empezando por el 0'''

anidada = ['alice', 25, ['python', 'react']]
print(anidada[2][0])

# si quieres sacar un elemento de una lista puedes hacerlo con *
# pero no modifica la lista original

ejemplo = ['juan', 25, 'programador']

name, *rest = ejemplo

print(name)
print(ejemplo)


# slice en listas

lista = ['mexico', 'argentina', 'peru', 'brazil', 'colombia']

print(lista[0:4])


# extraccion de intervalos

numeros = [1, 2, 3, 4, 5, 6, 7]
print(numeros[1::3])
