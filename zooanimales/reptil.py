from zooanimales.animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero,
                 colorEscamas = None, largoCola = None,  zona = None) -> None:
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        self._listado.append(self)

    @staticmethod
    def get_listado():
        return Reptil.listado

    @staticmethod
    def set_listado(listado):
        Reptil.listado = listado

    def get_color_escamas(self):
        return self.color_escamas

    def set_color_escamas(self, color):
        self.color_escamas = color

    def get_largo_cola(self):
        return self.largo_cola

    def set_largo_cola(self, largo):
        self.largo_cola = largo

    @staticmethod
    def cantidad_reptiles():
        return len(Reptil.listado)

    def movimiento(self):
        return "reptar"

    @staticmethod
    def crear_iguana(nombre, edad, genero, zona=None):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3, zona)

    @staticmethod
    def crear_serpiente(nombre, edad, genero, zona=None):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1, zona)
