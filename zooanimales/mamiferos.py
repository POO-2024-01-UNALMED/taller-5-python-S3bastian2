class Mamifero(animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, pelaje=None, patas=None, zona=None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.listado.append(self)

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
