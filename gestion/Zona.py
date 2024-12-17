class Zona:
    def __init__(self,nombre, zoo, animales):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = animales
        
    def agregarAnimales(self, animal):
        self._animales.append(animal)
        
    def cantidadAnimales(self):
        i = 0
        for animal in self._animales:
            if(animal != None):
                i += 1
        return i
    #Getters y Setters
    def getNombre(self):
        return self._nombre
    def getZoo(self):
        return self._zoo
    def getAnimales(self):
        return self._animales
    def setNombre(self, nombre):
        self._nombre = nombre
    def setZoo(self, zoo):
        self._zoo = zoo
    def setAnimales(self, animales):
        self._animales = animales