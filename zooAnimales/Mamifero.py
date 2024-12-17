from Animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0
    def __init__(self, nombre, edad, habitat, genero, zona, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.listado.append(self)
    
    def crearCaballo(nombre,edad,genero):
        Mamifero.caballos += 1
        caballo = Mamifero(nombre,edad, "pradera",genero,True,4)
    def crearLeon(nombre,edad,genero):
        Mamifero.leones += 1
        leon = Mamifero(nombre,edad, "selva",genero,True,4)
    def cantidadMamiferos():
        return len(Mamifero.listado)