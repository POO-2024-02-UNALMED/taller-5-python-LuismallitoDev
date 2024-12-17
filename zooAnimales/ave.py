from zooAnimales.animal import Animal
class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0
    
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPlumas=None):
        super().__init(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
        
    def crearHalcon(nombre, edad,genero):
        Ave.halcones += 1
        halcon =  Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        return halcon
    
    def crearAguila(nombre, edad, genero):
        Ave.aguilas += 1
        aguila = Ave(nombre, edad, "selva", genero, "blanco y amarillo")
        return aguila
    def cantidadAves():
        return len(Ave._listado)
    def movimiento():
        return "volar"
    
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
        return Ave._listado
    def set_listado( _listado):
        Ave._listado = _listado
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    def getHalcones():
        return Ave.halcones
    
    def setHalcones(halcones):
        Ave.halcones = halcones
    def getAguilas():
        return Ave.aguilas
    
    def setAguilas(aguilas):
        Ave.aguilas = aguilas