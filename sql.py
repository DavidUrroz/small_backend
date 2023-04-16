import sqlite3
from constantes import *

def conectar_db():
    conexion = sqlite3.connect(DATABASE_NAME)
    cursor = conexion.cursor()
    return conexion, cursor

def agregar_pelicula(pelicula):

    conexion, cursor = conectar_db()

    pelicula = (
        pelicula.nombre,
        pelicula.duracion,
        pelicula.genero
    )

    sql = f"INSERT INTO pelicula (nombre, duracion, genero) VALUES {pelicula};"
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def obtener_peliculas():
  conexion, cursor = conectar_db()

  sql = f"SELECT p.id, p.nombre, p.duracion, g.nombre as genero FROM pelicula p JOIN genero g ON p.genero = g.id;"
  cursor.execute(sql)
  peliculas = cursor.fetchall()
  conexion.close()
  return peliculas

def editar_peliculas(row, cambio, id):
   conexion, cursor = conectar_db()

   sql = f'UPDATE pelicula SET {row} = "{cambio}" WHERE id = {id};'
   cursor.execute(sql)
   conexion.commit()
   conexion.close()

def eliminar_pelicula(id):
   conexion, cursor = conectar_db()

   sql = f"DELETE FROM pelicula WHERE id = {id};"
   cursor.execute(sql)
   conexion.commit()
   conexion.close()