import parametros

# Menú de Inicio

def menu_inicio(dinero_disponible, ronda_actual):
     menu = f"""
                ∧ ,,, ∧    ~  ┏━━━━━━━━━━━━━━━━━━━━┓
               ( ̳• · • ̳)   ~ ♡    Menú de Inicio    ♡
               /      づ   ~  ┗━━━━━━━━━━━━━━━━━━━━━┛     

               DINERO : {dinero_disponible}  ═════════  RONDA : {ronda_actual}

                         [1] Tienda
                         [2] Ejercito
                         [3] Combatir

               [0] Salir 

     """
     print(menu)
     opcion = input("Escribe un número indicando tu opción del Menú:) \n")
     
     # Manejo de errores
     opciones_validas = ["0", "1", "2", "3"]
     
     while opcion not in opciones_validas:
          print("Opción inválida, por favor escoja nuevamente")
          print(menu)
          opcion = input("Escribe un número indicando tu opción del Menú:) \n")

     return int(opcion)

# Menú de Opción (1): Tienda

def menu_tienda(dinero_disponible):
     menu = f"""
               ¡Has seleccionado la opción de Tienda!
     
               DINERO = {dinero_disponible}

               Categoría  ═════════  Producto  ═════════  Precio

                                    [1] Gato Mago          {parametros.PRECIO_MAG}
               Gatos Combatientes   [2] Gato Guerrero      {parametros.PRECIO_GUE}
                                    [3] Gato Caballero     {parametros.PRECIO_CAB}
                         
                                    [4] Armadura           {parametros.PRECIO_ARMADURA}
               Ítems                [5] Pergamino          {parametros.PRECIO_PERGAMINO}
                                    [6] Lanza              {parametros.PRECIO_LANZA}
                    
               Curación             [7] Curar Ejército     {parametros.PRECIO_CURA}
               
               [0] Volver al Menú de Inicio
     """
     print(menu)
     opcion = input("Escribe un número indicando tu opción de la Tienda:) \n")
     
     # Manejo de errores
     opciones_validas = ["0", "1", "2", "3", "4", "5", "6", "7"]
     
     while opcion not in opciones_validas:
          print("Opción inválida, por favor escoja nuevamente")
          print(menu)
          opcion = input("Escribe un número indicando tu opción de la Tienda:) \n")

     return int(opcion)

# Menú de Selecciona un Gato

def selecciona_gato(gatos, item):

     opcion_valida = False

     while not opcion_valida:
          texto = f"""
                ¡Has seleccionado el ítem {item}!

             Selecciona el gato que deseas evolucionar

                        Nombre ═══ Clase
          """
          print(texto)
          
          for i in range(len(gatos)):
               print(f"                    [{i+1}] {gatos[i]._nombre}   ({gatos[i].tipo})")

          print("\n             [0] Volver al Menú de la Tienda \n")
          opcion = input("Escribe un número indicando tu selección de gato:) \n")

          # Manejo de errores
          opciones_validas = [str(i) for i in range(len(gatos) + 1)]
          
          if opcion not in opciones_validas:
               print("\n Opción inválida, por favor escoja nuevamente \n")

          else:
               opcion_valida = True

     return int(opcion)

# Textos 
def txt_enfrentamiento(combatiente, enemigo):
     texto = f"""
     Resumen del ataque

     {combatiente._nombre} 
          Vida: {round(combatiente.vida, 2)} - Poder: {round(combatiente.poder, 2)}
          Defensa: {round(combatiente.defensa, 2)} - Resistencia: {round(combatiente.resistencia, 2)}
          Agilidad: {round(combatiente.agilidad, 2)}
     {enemigo._nombre}
          Vida: {round(enemigo.vida, 2)} - Poder: {round(combatiente.poder, 2)}
          Defensa: {round(enemigo.defensa, 2)} - Resistencia: {round(enemigo.resistencia, 2)}
          Agilidad: {round(enemigo.agilidad, 2)}
     """
     print(texto)

def txt_ganador():
     texto = f"""
                       Ganaste esta ronda, felicidades!
               Avanzas a la siguiente ronda y ganas {parametros.ORO_GANADO} de oro:)
                                 ฅ^•ﻌ•^ฅ
     """
     return texto

def txt_perdedor():
     texto = f"""
                         Perdiste esta ronda:( 
               Vuelves a la ronda 1 con un ejercito vacío
     """
     return texto