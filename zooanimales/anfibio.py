class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, color_piel=None, venenoso=None, zona=None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self.color_piel = color_piel
        self.venenoso = venenoso
        Anfibio.listado.append(self)

    @staticmethod
    def get_listado():
        return Anfibio.listado

    @staticmethod
    def set_listado(listado):
        Anfibio.listado = listado

    def get_color_piel(self):
        return self.color_piel

    def set_color_piel(self, color_piel):
        self.color_piel = color_piel

    def is_venenoso(self):
        return self.venenoso

    def set_venenoso(self, venenoso):
        self.venenoso = venenoso

    @staticmethod
    def cantidad_anfibios():
        return len(Anfibio.listado)

    def movimiento(self):
        return "saltar"

    @staticmethod
    def crear_rana(nombre, edad, genero, zona=None):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True, zona)

    @staticmethod
    def crear_salamandra(nombre, edad, genero, zona=None):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False, zona)
