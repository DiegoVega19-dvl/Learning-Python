"""en python no existe un encapsulacion nativa como tal pero se puede simular
    declarando ya sea los metodos o atributos de la clase con dos guiones bajos"""


class Ejemplo:

    __atributo_privado = "esto es un ejemplo de atributo privado"

    def __metodo_privado(self):
        print("esto es un metodo privado")

    def metodo_publico(self):
        return self.__metodo_privado


e = Ejemplo()

print(e.metodo_publico)  # devuelve un error
