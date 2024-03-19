from zooanimales.animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero,
                 pelaje = None, patas = None, zona = None) -> None:
        super().__init__(nombre, edad, habitat, genero, zona) 
        self._pelaje = pelaje
        self._patas = patas
        self._listado.append(self)

    @staticmethod
    def get_listado():
        return Mamifero.listado

    @staticmethod
    def set_listado(listado):
        Mamifero.listado = listado

    def is_pelaje(self):
        return self.pelaje

    def set_pelaje(self, pelaje):
        self.pelaje = pelaje

    def get_patas(self):
        return self.patas

    def set_patas(self, patas):
        self.patas = patas

    @staticmethod
    def cantidad_mamiferos():
        return len(Mamifero.listado)

    @staticmethod
    def crear_caballo(nombre, edad, genero, zona=None):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4, zona)

    @staticmethod
    def crear_leon(nombre, edad, genero, zona=None):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4, zona)
