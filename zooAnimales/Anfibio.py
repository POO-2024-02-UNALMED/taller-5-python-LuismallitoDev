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
    def crearRana(nombre, edad,genero):
        Anfibio.ranas += 1
        rana = Anfibio(nombre,edad, "selva", genero,"rojo", True)
        return rana
    def crearSalamandra(nombre, edad, genero):
        Anfibio.salamandras += 1
        salamandra = Anfibio(nombre,edad, "selva", genero,"negro y amarilla", False)
        return salamandra
    def cantidadAnfibios():
        return len(Anfibio.listado)
    def movimiento():
        return "saltar"
        
    