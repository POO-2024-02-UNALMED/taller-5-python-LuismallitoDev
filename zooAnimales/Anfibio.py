from Animal import Animal
class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0
    def __init__(self, nombre, edad, habitat, genero, zona, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio.listado.append(self)