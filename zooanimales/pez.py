from zooanimales.animal import Animal

class Pez(Animal):
    _listado: list = []
    salmones: int = 0
    bacalaos: int = 0

    def __init__(self, nombre, edad, habitat, genero,
                 colorEscamas = None, cantidadAletas = None, zona = None) -> None:
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
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

    def getCantidadAletas(self):
        return self._cantidadAletas
    def setCantidadAletas(self, cantidad):
        self._cantidadAletas = cantidad

    @staticmethod
    def cantidadPeces():
        return Pez._totalAnimales

    def movimiento(self):
        pass

    @staticmethod
    def crearSalmon(nombre, edad, genero, zona = None):
        Pez.salmones += 1
        return Pez(nombre, edad, "oceano", genero, zona,
                 "rojo", 6)

    def crearBacalao(nombre, edad, genero, zona = None):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, zona,
                 "gris", 6)