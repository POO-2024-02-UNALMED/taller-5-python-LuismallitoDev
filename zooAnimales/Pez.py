from Animal import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre, edad, habitat, genero, zona, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas