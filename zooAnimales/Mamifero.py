from Animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0
    def __init__(self, nombre, edad, habitat, genero, zona, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)
    
    def crearCaballo(nombre,edad,genero):
        Mamifero.caballos += 1
        caballo = Mamifero(nombre,edad, "pradera",genero,True,4)
        return caballo
    def crearLeon(nombre,edad,genero):
        Mamifero.leones += 1
        leon = Mamifero(nombre,edad, "selva",genero,True,4)
        return leon
    def cantidadMamiferos():
        return len(Mamifero._listado)
    
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
        return Mamifero._listado
    def set_listado( _listado):
        Mamifero._listado = _listado
    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    def getPatas(self):
        return self._patas
    
    def setPatas(self, patas):
        self._patas = patas
    def setLeones(leones):
        Mamifero.leones = leones
    def getCaballos(caballos):
        Mamifero.caballos = caballos
    def getLeones(leones):
        return Mamifero.leones
    