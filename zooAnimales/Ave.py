from Animal import Animal
class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0
    
    def __init__(self, nombre, edad, habitat, genero, zona, colorPlumas):
        super().__init(nombre, edad, habitat, genero, zona)
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)