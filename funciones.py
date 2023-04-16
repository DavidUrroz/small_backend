from modelos import Pelicula, Genero, Catalogo
import sql

def agregar_pelicula():
  nombre = str(input('Ingrese el nombre de la película: '))
  duracion = float(input('Ingrese la duración de la película en minutos: '))
  genero = int(input('Ingrese el género de la película: '))


  pelicula = Pelicula(nombre, duracion, genero)

  sql.agregar_pelicula(pelicula)

catalogo = Catalogo('Peliculas de Mafia')

def obtener_peliculas():
  peliculas_db = sql.obtener_peliculas()
  peliculas_nuevas = []
  for pelicula in peliculas_db:
    guardar_pelicula = Pelicula(pelicula[1], pelicula[2],pelicula[3])
    # guardar_pelicula = Pelicula(pelicula[1], pelicula[2],pelicula[3])
    if guardar_pelicula not in catalogo.peliculas:
      peliculas_nuevas.append(guardar_pelicula)

  catalogo.peliculas.extend(peliculas_nuevas)

  contador = 0
  for pelicula in catalogo.peliculas:
    print(f"""
ID de la película: {peliculas_db[contador][0]}
Nombre de la película: {pelicula.nombre}
Duración de la película: {pelicula.duracion} minutos
Género de la película: {pelicula.genero}""")
    contador +=1
    

def editar_pelicula():
  id = int(input('Ingrese el ID de la pélicula a cambiar: '))
  peliculas_db = sql.obtener_peliculas()
  peliculas_ids = [p[0] for p in peliculas_db]
  if id not in peliculas_ids:
    print(f'La película con el ID {id} no existe')
    return
  row = int(input("""¿Qué deseas cambiar? 
1. Nombre
2. Duración
3. Género
- """))
  if row == 1:
    tabla = 'nombre'
    cambio = str(input('Ingrese el nuevo nombre de la película: '))
    sql.editar_peliculas(tabla,cambio,id)
    print('Se ha realizado el cambio correctamente')
  elif row == 2:
    tabla = 'duracion'
    cambio = int(input('Ingrese la nueva duración de la película: '))
    sql.editar_peliculas(tabla,cambio,id)
    print('Se ha realizado el cambio correctamente')
  elif row == 3:
    tabla = 'genero'
    cambio = int(input('Ingrese el ID de la nuevo género de la película: '))
    sql.editar_peliculas(tabla,cambio,id)
    print('Se ha realizado el cambio correctamente')
  else:
    print(f'La opción: {row} no existe')
    
  # else:
  #   print(f'La película con el ID {id} no existe')


def eliminar_pelicula():
  id = int(input('Ingrese el ID de la pélicula a ELIMINAR: '))
  id_2 = id
  peliculas_db = sql.obtener_peliculas()
  peliculas_ids = [p[0] for p in peliculas_db]
  if id not in peliculas_ids:
    print(f'La película con el ID {id} no existe')
    return
  else:
    sql.eliminar_pelicula(id)
    print(f'La película con el {id_2} se ha eliminado')

