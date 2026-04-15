numero = 15
texto = "esto es un texto"

c = "{} es un numero y {} es un texto".format(numero, texto)

print(c)


"""esto es una otra forma de concatenar variables con cadenas de texto con el metodo format"""

print("{numero}, {numero}, {numero}".format(numero=numero))

# alinamiento a la derecha 15 espacios con trucamiento
print("{:>15.1}".format("hola"))


# formateo de numeros enteros

print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

# formateo de numeros flotantes, rellenados con espacios

print("{:.4f}".format(3.141626))

# alinear numeros decimales
print("{:7.3f}".format(3.141626))
print("{:7.3f}".format(153.45))
