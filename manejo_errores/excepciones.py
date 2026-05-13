"""def dividir(a, b):
    try:
        return a/b
    except:
        print("no se puede dividir entre cero")


print(dividir(20, 0)) """

while (True):
    try:
        n = int(input("introduce un numero: "))
        m = int(input("introduce otro numero: "))
        print(n/m)
        break
    except Exception as e:
        print(type(e).__name__)
