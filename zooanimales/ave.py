from zooanimales.animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, color_plumas=None, zona=None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self.color_plumas = color_plumas
        Ave.listado.append(self)

    @staticmethod
    def get_listado():
        return Ave.listado

    @staticmethod
    def set_listado(listado):
        Ave.listado = listado

    def get_color_plumas(self):
        return self.color_plumas

    def set_color_plumas(self, color):
        self.color_plumas = color

    @staticmethod
    def cantidad_aves():
        return len(Ave.listado)

    def movimiento(self):
        return "volar"

    @staticmethod
    def crear_halcon(nombre, edad, genero, zona=None):
        Ave.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso", zona)

    @staticmethod
    def crear_aguila(nombre, edad, genero, zona=None):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo", zona)
