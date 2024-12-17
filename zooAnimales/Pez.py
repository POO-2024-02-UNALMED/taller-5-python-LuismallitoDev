from Animal import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre, edad, habitat, genero, zona, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
    def movimiento():
        return "nadar"
    def crearSalmon(nombre,edad,genero):
        Pez.salmones += 1
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        return salmon
    def crearBacalao(nombre,edad,genero):
        Pez.bacalaos += 1
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        return bacalao
    def cantidadPeces():
        return len(Pez.listado)