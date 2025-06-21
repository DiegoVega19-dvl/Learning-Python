# ejercicios con estructuras de control con python

print("bienvenido a la suma de dos numeros")
num1 = int(input("ingresa un numero: "))
num2 = int(input("igresa un segundo numero: "))

if num1 > num2:
    print("el numero " + str(num1) + " es mayor que " + str(num2))
elif num1 == num2:
    print("ambos numeros son iguales")
else:
    print("el numero " + str(num2) + " es mayor que " + str(num1))


# sumas basicas

numero1 = int(input("Coloca tu primer numero: "))
numero2 = int(input("Coloca tu segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print("El resultado de la suma es:", suma)
print("El resultado de la resta es:", resta)
print("El resultado de la multiplicación es:", multiplicacion)
print("El resultado de la división es:", division)
