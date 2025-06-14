# condicional if-else

# es el if de toda la vida funciona igual

num1 = 10
num2 = 20

if num1 >= True:
    print("El primer numero es mayor")
else:
    print("El segundo numero es mayor")

# elif

# se usa elif si quieres anidar un if, no se anida comunmente contro otro if como en otros lenguajes, eso puede generar conflictos
# chorradas de python xd

x = 1

if x == 50:
    print("x es igual a 50")
elif x == 80:
    print("x es igual a 80")
elif x == 90:
    print("x es igual a 90")
elif x == 100:
    print("x es igual a 100")
else:
    print("x no es ninguno de los valores anteriores")


# bucle for, funciona un poco diferente a los fors convencionales

lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]

for i in lista:
    for j in i:
        print(j)
        


# slicing

texto = "hola mundo"

for i in texto[::-1]:
    print(i, end="")
