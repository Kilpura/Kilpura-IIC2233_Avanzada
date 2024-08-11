import menus
import entidades
import sys
import parametros
import funciones

# Inicio del programa
salida = False

if len(sys.argv) != 2:
     print("Debe ingresar solo una dificultad, intente nuevamente")
     salida = True
else:
     dificultad = sys.argv[1]
     if dificultad in parametros.RUTAS_DIFICULTAD:
          ejercito_enemigo = funciones.cargar_ejercitos(dificultad)

dinero_disponible = parametros.ORO_INICIAL
dinero_ganado = parametros.ORO_GANADO
ronda_actual = 1

ejercito_combatiente = entidades.Ejercito([])

while not salida and ronda_actual <= 3:
     opcion_inicio = menus.menu_inicio(dinero_disponible, ronda_actual)

     if opcion_inicio == 0:
          print("Gracias por jugar:)")
          salida = True
     
     elif opcion_inicio == 1:
          #Se abre el menu tienda
          opcion_tienda = menus.menu_tienda(dinero_disponible)

          if opcion_tienda == 0:
               continue

          elif opcion_tienda == 1:
               dinero_disponible = funciones.comprar_gato(1, dinero_disponible, ejercito_combatiente)
          
          elif opcion_tienda == 2:
               dinero_disponible = funciones.comprar_gato(2, dinero_disponible, ejercito_combatiente)

          elif opcion_tienda == 3:
               dinero_disponible = funciones.comprar_gato(3, dinero_disponible, ejercito_combatiente)
          
          elif opcion_tienda == 4:
               dinero_disponible = funciones.comprar_item(4, dinero_disponible, ejercito_combatiente)
          
          elif opcion_tienda == 5:
               dinero_disponible = funciones.comprar_item(5, dinero_disponible, ejercito_combatiente)
          
          elif opcion_tienda == 6:
               dinero_disponible = funciones.comprar_item(6, dinero_disponible, ejercito_combatiente)
          
          elif opcion_tienda == 7:
               dinero_disponible = funciones.curar_ejercito(dinero_disponible, ejercito_combatiente)

     elif opcion_inicio == 2:
          # se muestra el ejercito
          print(ejercito_combatiente)
     
     elif opcion_inicio == 3:
          for ejercito in ejercito_enemigo:
               enemigo = entidades.Ejercito(ejercito)
               ganador = ejercito_combatiente.combatir(enemigo)

               if ganador:
                    print(menus.txt_ganador())
                    ronda_actual += 1
                    dinero_disponible += parametros.ORO_GANADO
                    break  # Salimos del bucle de combate y pasamos a la siguiente ronda
               else:
                    print(menus.txt_perdedor())
                    ronda_actual = 1
                    ejercito_combatiente = entidades.Ejercito([])
                    break  # Salimos del bucle de combate y volvemos al menú principal
print("¡Has completado las tres rondas!")