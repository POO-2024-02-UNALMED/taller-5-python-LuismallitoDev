from zooAnimales.animal import Animal
class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, largoCola=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)
    def movimiento():
        return "reptar"
    
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
        return Reptil._listado
    def set_listado( _listado):
        Reptil._listado = _listado
    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
    def getIguanas(self):
        return Reptil.iguanas
    
    def setIguanas(self, iguanas):
        Reptil.iguanas = iguanas
    def getSerpientes(self):
        return Reptil.serpientes
    
    def setSerpientes(self, serpientes):
        Reptil.serpientes = serpientes
    
