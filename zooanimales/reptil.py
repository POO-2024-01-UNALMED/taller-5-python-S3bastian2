from zooanimales.animal import Animal

class Reptil(Animal):
    _listado: list = []
    iguanas: int = 0
    serpientes: int = 0

    def __init__(self, nombre, edad, habitat, genero,
                 colorEscamas = None, largoCola = None,  zona = None) -> None:
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        self._listado.append(self)

    @classmethod
    def getListado(cls):
        return cls._listado
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getLargoCola(self):
        return self._largoCola
    def setLargoCola(self, largo):
        self._largoCola = largo

    @staticmethod
    def cantidadReptiles():
        return Reptil._totalAnimales

    def movimiento(self):
        pass

    @staticmethod
    def crearIguana(nombre, edad, genero, zona = None):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, zona,
                 "verde", 3)

    def crearSerpiente(nombre, edad, genero, zona = None):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, zona,
                 "blanco", 1)

