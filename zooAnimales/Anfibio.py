from Animal import Animal
from gestion import *
class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0
    def __init__(self, nombre, edad, habitat, genero, zona, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
    def crearRana(nombre, edad,genero):
        Anfibio.ranas += 1
        rana = Anfibio(nombre,edad, "selva", genero,"rojo", True)
        return rana
    def crearSalamandra(nombre, edad, genero):
        Anfibio.salamandras += 1
        salamandra = Anfibio(nombre,edad, "selva", genero,"negro y amarilla", False)
        return salamandra
    def cantidadAnfibios():
        return len(Anfibio._listado)
    def movimiento():
        return "saltar"
        
    #Getters y setters
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
    def get_listado():
        return Anfibio._listado
    def set_listado( _listado):
        Anfibio._listado = _listado
    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel
    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
    def getRanas():
        return Anfibio.ranas
    
    def setRanas(ranas):
        Anfibio.ranas = ranas
    def getSalamandras():
        return Anfibio.salamandras
    def setSalamandras(salamandras):
        Anfibio.salamandras = salamandras