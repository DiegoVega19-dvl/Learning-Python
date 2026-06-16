'''la funcion zip es una forma de combinar dos o mas listas, tuplas o diccionarios en una sola estructurar. esta funcion es util para cuando se necesita iterar sobre un conjunto de elementos y requieres tener acceso a los elementos de cada una de las estructuras de datos a lavez. esta funcion tambien es util para cuando necesites combinar dos o mas listas para crear una nueva lista'''

desarrolladores = ['diego', 'ana', 'pedro']
codigo = [1, 2, 3]

# print(list(zip(desarrolladores, codigo)))

# ejemplo con ciclo for

for name, id in zip(desarrolladores, codigo):
    print(f'name: {name}')
    print(f'Id: {id}')
