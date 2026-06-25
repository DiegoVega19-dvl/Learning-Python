'''los conjuntos son una de las estructuras de datos integradas en python. una de las caracteristicas principales de los conjuntos es que no alamcenan valores duplicados. si intentas agregar un valor duplicado a un conjuntom solo se almacenar uno de ellos'''


'''los conjuntos son mutables y no ordenados, lo que significa que sus elementos no se almacenan en un orden especifico, por lo que no puedes usar indices o claves para acceder a ellos. solo pueden contener valores de tipos de datos inmutables como numeros, cadenas y tuplas. ademas, soportan operaciones matematicas de conjuntos, incluyendo union, interseccion, diferencia y diferencia simetrica'''


# definicion

ejemplo_set = {1, 2, 3, 4, 5}

'''dato: si estamos trabajando con conjuntos, y si da la casualidad de definir un conjunto vacio, debemos hacerlo con el constructor set(). por que si lo declaras con {} vacias, python automaticamente lo detectara como un diccionario'''

set_vacio = {}

print(type(set_vacio))  # salida: dict()
