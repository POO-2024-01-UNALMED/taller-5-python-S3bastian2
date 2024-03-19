from zooanimales.animal import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero,
                 colorEscamas = None, cantidadAletas = None, zona = None) -> None:
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        self._listado.append(self)

    @staticmethod
    def get_listado():
        return Pez.listado

    @staticmethod
    def set_listado(listado):
        Pez.listado = listado

    def get_color_escamas(self):
        return self.color_escamas

    def set_color_escamas(self, color):
        self.color_escamas = color

    def get_cantidad_aletas(self):
        return self.cantidad_aletas

    def set_cantidad_aletas(self, cantidad):
        self.cantidad_aletas = cantidad

    @staticmethod
    def cantidad_peces():
        return len(Pez.listado)

    def movimiento(self):
        return "nadar"

    @staticmethod
    def crear_salmon(nombre, edad, genero, zona=None):
        Pez.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6, zona)

    @staticmethod
    def crear_bacalao(nombre, edad, genero, zona=None):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6, zona)
