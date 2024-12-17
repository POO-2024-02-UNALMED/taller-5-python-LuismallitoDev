class Zoologico:
    def __init__(self, nombre=None, ubicacion=None, zonas=None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas if zonas is not None else []
    
    def agregarZonas(self,zona):
        self._zonas.append(zona)
    
    def cantidadTotalAnimales(self):
        i = 0
        for zona in self._zonas:
            i += zona.cantidadAnimales()
        return i
    #Getters y Setters
    def setNombre(self, nombre):
        self._nombre = nombre
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    def setZona(self,zonas):
        self._zonas = zonas
    def getNombre(self):
        return self._nombre
    def getUbicacion(self):
        return self._ubicacion
    def getZona(self):
        return self._zonas