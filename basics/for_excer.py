list = [1, 2, 3, 4, 5]

for i in list:
    print(i)


for i in range(0, 5):
    print(i)


for item in ["platano", "pera", "sandia"]:
    print(item)


diccionario = {
    "juan": 25,
    "jose": 20,
    "pedro": 22,
}

for estudiantes, edad in diccionario.items():
    print(estudiantes, "->", edad)


frutas = ["manzana", "pera", "sandia", "naranja"]
objetivo = "agucate"

for fruta in frutas:
    print("escanenado", fruta)
    if fruta == objetivo:
        print("fruta localizada: ", objetivo)
        break
else:
    print("fruta no localizada :( ")
