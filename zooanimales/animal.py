import zooanimales

class Animal:
    _totalAnimales: int = 0
    _listado = []
    def __init__(self, nombre, edad, habitat, genero, zona = None) -> None:
        self._nombre =nombre
        self._edad = edad
        self._habitat = habitat
        self._genero  = genero
        self._zona = zona #0 ó 1
        Animal._totalAnimales += 1
        Animal._listado.append(self)

    def getTotalAnimales(self):
        return self._totalAnimales
    def setNombre(self, totalAnimales):
        self._totalAnimales = totalAnimales
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getEdad(self):
        return self._edad
    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat
    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero
    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona
    def setZona(self, zona):
        self._zona = zona

    def movimiento():
        pass

    @classmethod
    def totalPorTipo(cls):
        totalPorTipo: str = ""
        contador = 0
        for x in [zooanimales.mamifero.Mamifero, 
                  zooanimales.ave.Ave, 
                  zooanimales.reptil.Reptil, 
                  zooanimales.pez.Pez, 
                  zooanimales.anfibio.Anfibio]:
            nombre = ["Mamiferos", "Aves", "Reptiles", "Peces", "Anfibios"]
            totalPorTipo += f"{nombre[contador]} : {len(x.getListado())}\n"
            contador += 1
        return totalPorTipo

    def toString(self) -> str:
        if self._zona:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona._nombre}, en el {self._zona._zoo._nombre}"
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
