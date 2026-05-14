"""class Automovil:
    # constructor de la clase
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    # metodo
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")


class Motocicleta:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color


# Crear una instancia de la clase Automovil
mi_auto = Automovil("Toyota", "Corolla", 2020)
# Mostrar la información del automóvil
mi_auto.mostrar_informacion()"""


class Pelicula:
    def __init__(self, titulo, duracion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self. genero = genero

    def __str__(self):
        return '{}({})'.format(self.titulo, self.duracion)


class Catalogo:
    peliculas = []

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)


peli = Pelicula("Naufrago", 143, "supervivencia")
peli2 = Pelicula("Atrapame si puedes", 141, "Caper")

cata = Catalogo([peli])
cata.agregar(Pelicula("atrapame si puedes", 141, "drama"))
print(cata.mostrar())
