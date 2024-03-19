import zooanimales

class Animal:
    total_animales = 0
    listado = []

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, zona=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = zona
        Animal.total_animales += 1
        Animal.listado.append(self)

    @staticmethod
    def get_listado():
        return Animal.listado

    @staticmethod
    def get_total_animales():
        return Animal.total_animales

    @staticmethod
    def set_total_animales(total_animales):
        Animal.total_animales = total_animales

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_habitat(self):
        return self.habitat

    def set_habitat(self, habitat):
        self.habitat = habitat

    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero

    def get_zona(self):
        return self.zona

    def set_zona(self, zona):
        self.zona = zona

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def total_por_tipo():
        return "Mamiferos: {}\nAves: {}\nReptiles: {}\nPeces: {}\nAnfibios: {}".format(
            len(Mamifero.get_listado()),
            len(Ave.get_listado()),
            len(Reptil.get_listado()),
            len(Pez.get_listado()),
            len(Anfibio.get_listado())
        )

    def __str__(self):
        if self.zona:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}, la zona en la que me ubico es {self.zona.get_nombre()}, en el {self.zona.get_zoo().get_nombre()}"
        else:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}"
