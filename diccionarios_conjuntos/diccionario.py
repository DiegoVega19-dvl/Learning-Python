'''en python los diccionarios son estructuras de datos integradas que almacenan colecciones de pares clave-valor. funcionan de manera similar a los diccionarios reales, donde buscas una palabra para encontrar si significado correspondiente'''

# sintaxis

usuario = {
    "nombre": "juan",
    "edad": 25,
    "grado": "licenciatura"
}

# mismo ejemplo usando el constructor dict()

ejemplo = dict([('nombre', 'diego'), ('edad', 25), ('grado', 'licenciatura')])


print(usuario['nombre'])

print(usuario.get('nombre'))

# los metodos key y values devulven un objetos con sus respectivos valores

print(usuario.keys())

print(usuario.values())

# el metodo item devuelve un objeto vista con todos los pares clave-valor en el diccionario. incluyendo tanto las claves como los valores.

print(usuario.items())


# el metodo clear elimina todos los paraes calve-valor del diccionario

# print(usuario.clear())

# el metodo pop elimina el par clave-valor con la clave que especifiques como primer argumento y devulve su valor, si la clave no existe, devuelve el valor predeterminado que especificas como segundo argumento. la si la clave no existe y no pasas un valor predeterminado,se generara un keyError


print(usuario.pop('nombre', "juan"))

print(usuario)

# en python 3.7 y posteriores el metodo popitem elimina el ultimo elemento insertado
