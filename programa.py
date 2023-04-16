import funciones

while True:
   
  try:
      menu = int(input("""
1. Agregar nueva película
2. Obtener película
3. Editar película
4. Eliminar película
0. Salir del programa
- """))
      if menu == 1:
          funciones.agregar_pelicula()
      elif menu == 2:
          funciones.obtener_peliculas()
      elif menu == 3:
          funciones.editar_pelicula()
      elif menu == 4:
          funciones.eliminar_pelicula()
      elif menu == 0:
          print('Saliendo del programa')
          exit()
      else:
          print(f'La opción {menu} no existe')
  except ValueError as error:
       print(f'Ingrese una opción válida, {error}\n')