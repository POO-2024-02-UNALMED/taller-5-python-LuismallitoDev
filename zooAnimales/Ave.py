from Animal import Animal
class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0
    
    def __init__(self, nombre, edad, habitat, genero, zona, colorPlumas):
        super().__init(nombre, edad, habitat, genero, zona)
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)
        
    def crearHalcon(nombre, edad,genero):
        Ave.halcones += 1
        halcon =  Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        return halcon
    
    def crearAguila(nombre, edad, genero):
        Ave.aguilas += 1
        aguila = Ave(nombre, edad, "selva", genero, "blanco y amarillo")
        return aguila
    def cantidadAves():
        return len(Ave.listado)
    def movimiento():
        return "volar"