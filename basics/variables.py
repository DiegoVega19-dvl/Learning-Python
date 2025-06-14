
# tipos de datos en python

# cadena de texto (string)
cadena = "esto es una cadena de texto"

# entero (integer)
entero = 123

# flotante (float)
flotante = 123.456

# booleano (boolean)
booleano = True

# nulo (None)
nulo = None

# lista (list)
lista = [1, 2, 3, 4, 5]

# diccionario
diccionario = {
    "clave1": "valor1",
    "clave2": "valor2",
    "clave3": "valor3"
}

# tupla
tupla = (1, 2, 3, 4, 5)

# conjunto
conjunto = {1, 2, 3, 4, 5}


print(diccionario)



"""tipos de datos"""


# entero o int

numero = -100 # los int en python permiten almacenar numero enteros no decimal positivos o negativos
numero1 = 100

# ejemplos tipos de dato int

a = 0b100 # el 0b indica que el numero es decimal
b = 0x17 # el 0x indica que el numero es hexadecimal
c = 0o720 # el 0o indica que el numero es octal

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))


# bool o booleano

x = True
y = False

# un valor booleano tambien puede ser le resultado deevaluar un expresion

print(1 > 0)
print(1 <= 0)
print(9 == 9)


if 1<=0:
    print('es true')
else:
    print('es false')



# float

decimal = 12.20 # en python los numeros decimales son de tipo float que en realidad son de tipo double
print(type(decimal))

f = 1.93e-3 # tambien puede declarar variables con notacion cientifica 'e'


# en python no tiene presicion infinita
presision = 0.99999999999999999999999999
print(presision) # resultado 1


# numeros complejos en python


complejo = 3 + 5j
print(type(complejo))

print(complejo.real) # es posible acceder a la parte real usando le metodo real
print(complejo.imag) # y a la parte imaginaria usando el metodo imag

# tambien se puede declarar una variables de tipo complejo usando la funcion complex

com = complex(3,5)
print(com)

# suma de complejos

a = 1 + 3j
b = 4 + 1j
print(a+b)

# en la aritmetica complex se suma la parte reale por seperado e igual la parte imaginaria

# repasar aritmetica y algebra
# echarle un ojo a la libreria cmath

# =========================================================================================================================
# =========================================================================================================================


# strings o cadenas

cadena = 'esto es una cadena texto'

# las cadenas de texto de tipo inmutable

# el simbolo \ nos permite incrustar comillas dentro de una cadena de texto

# con la letra 'r' antes de comenzar la cadena, ignora todos los prefijos e imprime en bruto

# metodos de string, investigar luego


# =========================================================================================================================
# =========================================================================================================================



# estructuras











