import Mamifero
import Ave
import Anfibio
import Reptil 
import Pez
class Animal():
    totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero, zona):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal.totalAnimales += 1
    def getTotalAnimales():
        return Animal.totalAnimales
    def totalPorTipo():
        return ("Mamiferos: " + Mamifero.cantidadMamiferos() + "\n" +
                "Aves: " + Ave.cantidadAves() + "\n" +
                "Reptiles: " + Reptil.cantidadReptiles() + "\n" +
                "Peces: " + Pez.cantidadPeces() + "\n" +
                "Anfibios: " + Anfibio.cantidadAnfibios()
                )
    def movimiento():
        return "desplazarse"
    def toString(self):
        if(self._zona != None):
            return(
                "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat
                    + " y mi genero es " + self._genero + "la zona en la que me ubico es " + self._zona + ", en el "
                    + self._zona.getZoo()
            )
        else:
            return(
                "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat
                    + " y mi genero es " + self._genero
            )
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
    