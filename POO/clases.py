class Automovil:
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


# Crear una instancia de la clase Automovil
mi_auto = Automovil("Toyota", "Corolla", 2020)
# Mostrar la información del automóvil
mi_auto.mostrar_informacion()
