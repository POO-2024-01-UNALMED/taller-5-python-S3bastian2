from zooanimales.animal import Animal

class Anfibio(Animal):
    _listado: list = []
    ranas: int = 0
    salamandras: int = 0
    
    def __init__(self, nombre, edad, habitat, genero,
                 colorPiel = None, venenoso = None, zona = None) -> None:
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        self._listado.append(self)

    @classmethod
    def getListado(cls):
        return cls._listado
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self, color):
        self._colorPiel = color

    def isVenenoso(self):
        return self._venenoso
    def setVenenoso(self, venenoso):
        self._venenoso= venenoso

    @staticmethod
    def cantidadAnfibios(self):
        Anfibio._totalAnimales

    def movimiento(self):
        pass

    @staticmethod
    def crearRana(nombre, edad, genero, zona = None):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, zona,
                 "rojo", True)

    @staticmethod
    def crearSalamandra(nombre, edad, genero, zona = None):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, zona,
                 "negro y amarillo", False)
