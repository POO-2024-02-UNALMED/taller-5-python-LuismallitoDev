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
        