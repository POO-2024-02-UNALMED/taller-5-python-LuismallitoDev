import Animal
class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre, edad, habitat, genero, zona, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.listado(self)
    def movimiento():
        return "reptar"
