class Pelicula:
    def __init__(self,nombre,duracion, genero):
        # self.id = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
    
    def __eq__(self, other):
      if isinstance(other, Pelicula):
        return (self.nombre == other.nombre
                and self.duracion == other.duracion
                and self.genero == other.genero)
      return False

class Genero:
    def __init__(self, nombre):
        self.nombre = nombre

class Catalogo:
    def __init__(self,nombre):
        self.nombre = nombre
        self.peliculas = []