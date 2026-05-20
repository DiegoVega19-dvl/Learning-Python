'''cadena = "hola mundo"

print("h" in cadena)


# para saber la longitud de una cadena, podemos usar el metodo len

print(len(cadena))  # salida: 10

# indexacion de caracteres

print(cadena[-1])


# interpolacion de cadenas, es el proceso de porder insertar cadenas con operaciones

edad = 25
nombre = 'Diego'

print(f"hola me llamo {nombre} y tengo {edad}")

# corte de cadenas (slicing)

ejemplo = "esto es una cadena"

print(ejemplo[1:3])  # salida: st

# cortar una cadena no modifica la original'''


# metodos para cadenas


cadena_ejemplo = "esto es Una Cadena"

# ha varios pero estos son unos ejemplos

# upper convierte toda la cadena a mayusculas
nuevo_ejemplo = cadena_ejemplo.upper()
print(nuevo_ejemplo)

# lower convierte toda la cadena a minusculas
otro_ejemplo = cadena_ejemplo.lower()
print(otro_ejemplo)

# capitalize convierte la primera letra a mayusculas y las demas a minusculas

ultimo_ejemplo = cadena_ejemplo.capitalize()
print(ultimo_ejemplo)


# // sirve para divisiones enteras
numero = 10
numero2 = 10

numero3 = numero // numero2
print(numero3)


# metodos para numeros enteros y flotantes

# round()

'''redondea un numero a un numero especificado de lugares decimales'''

# abs()

'''devuelve el valor absoluto de un numero'''

# pow()

'''eleva un numero a la ptencia de otro o realiza exponenciacion modular'''

result_1 = pow(2, 3)  # regresa la potencia
print(result_1)

# regresa el residuo de la potencia dada de lo primero dos elementos % 5
result_2 = pow(2, 3, 5)
print(result_2)
