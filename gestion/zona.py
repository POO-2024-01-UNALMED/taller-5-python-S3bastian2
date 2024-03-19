class Zona:
    def __init__(self, nombre, zoo = None) -> None:
        self._nombre: str = nombre
        self._zoo = zoo #Solo 1
        self._animales = [] #0 ó más

    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getZoo(self):
        return self._zoo
    def setZoo(self, zoo):
        self._zoo = zoo

    def getAnimales(self):
        return self._animales
    def setAnimales(self, animal):
        self._animales.append(animal)

    def agregarAnimales(self, animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        return len(self._animales)
