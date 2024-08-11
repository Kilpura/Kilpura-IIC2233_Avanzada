import parametros
import entidades
import os.path
import random
import menus

def validar_atributos(atributos):
     #Verificar que hayan 7 atributos
     if len(atributos) != 7:
          print("\n Faltan atributos para uno de tus Gatos \n")
          return False

     if atributos[0].isdigit():
          print(f"\n El formato de nombre para uno de tus Gatos no es válido \n")
          return False

     if atributos[1].isalpha():
          if atributos[1] not in parametros.TIPOS_COMBATIENTES:
               print(f"\n El tipo de combatiente de uno de tus Gatos no es válido \n")
               return False
     else:
          print(f"\n El tipo de combatiente de uno de tus Gatos no es válido \n")
          return False

     if not atributos[2].isdigit():
          print("\n El formato de la vida máxima de uno de tus Gatos no es válido \n")
          return False
    
     elif not 0 <= int(atributos[2]) <= 100:
          print("\n La vida máxima para uno de tus Gatos no es válida \n")
          return False

     if not atributos[3].isdigit():
          print("\n El formato de la defensa de uno de tus Gatos no es válido \n")
          return False
    
     elif not 1 <= int(atributos[3]) <= 20:
          print("\n La defensa para uno de tus Gatos no es válida \n")
          return False

     if not atributos[4].isdigit():
          print("\n El formato del poder de uno de tus Gatos no es válido \n")
          return False
    
     elif not 1 <= int(atributos[4]) <= 10:
          print("\n El poder para uno de tus Gatos no es válida \n")
          return False

     if not atributos[5].isdigit():
          print("\n El formato de la agilidad de uno de tus Gatos no es válido \n")
          return False
    
     elif not 1 <= int(atributos[5]) <= 10:
          print("\n La agilidad para uno de tus Gatos no es válida \n")
          return False

     if not atributos[6].isdigit():
          print("\n El formato de la resistencia de uno de tus Gatos no es válido \n")
          return False
    
     elif not 1 <= int(atributos[6]) <= 10:
          print("\n La resistencia para uno de tus Gatos no es válida \n")
          return False

     return True

def cargar_ejercitos(dificultad):
     path = parametros.RUTAS_DIFICULTAD[dificultad]
     ejercitos = []

     # Verificar si el archivo existe
     if not os.path.exists(path):
          print("\n El archivo seleccionado no existe :/ \n")
          return False
     
     with open(path, 'r') as file:
          lineas = file.readlines()

          for linea in lineas:
               # Los gatos se encuentran separados por ;
               gatos = linea.strip().split(";")
               combatientes = []

               for datos_gato in gatos:
                    atributos = datos_gato.split(",")

                    if not validar_atributos(atributos):
                         return False
   
                    nombre = atributos[0]
                    tipo = atributos[1]
                    vida_maxima = int(atributos[2])
                    defensa = int(atributos[3])
                    poder = int(atributos[4])
                    agilidad = int(atributos[5])
                    resistencia = int(atributos[6])

                    # Crear instancias de las subclases correspondientes
                    if tipo == "GUE":
                         combatiente = entidades.Guerrero(nombre, vida_maxima, vida_maxima, poder, defensa, agilidad, resistencia)
                    elif tipo == "MAG":
                         combatiente = entidades.Mago(nombre, vida_maxima, vida_maxima, poder, defensa, agilidad, resistencia)
                    elif tipo == "CAB":
                         combatiente = entidades.Caballero(nombre, vida_maxima, vida_maxima, poder, defensa, agilidad, resistencia)
                    elif tipo == "PAL":
                         combatiente = entidades.Paladin(nombre, vida_maxima, vida_maxima, poder, defensa, agilidad, resistencia)
                    elif tipo == "MDB":
                         combatiente = entidades.MagoBatalla(nombre, vida_maxima, vida_maxima, poder, defensa, agilidad, resistencia)
                    elif tipo == "CAR":
                         combatiente = entidades.CaballeroArcano(nombre, vida_maxima, vida_maxima, poder, defensa, agilidad, resistencia)

                    combatientes.append(combatiente)
               
               ejercitos.append(combatientes)
     return ejercitos

def cargar_unidad():
     path = "data/unidades.txt"

    # Verificar si el archivo existe
     if not os.path.exists(path):
          print("\n El archivo de unidades no existe :/ \n")
          return False
     
     gatos = []
     with open(path, 'r') as file:
          lineas = file.readlines()

          for linea in lineas:
               atributos = linea.strip().split(",")

               if not validar_atributos(atributos):
                    return False
               
               nombre = atributos[0]
               tipo = atributos[1]
               vida_maxima = int(atributos[2])
               defensa = int(atributos[3])
               poder = int(atributos[4])
               agilidad = int(atributos[5])
               resistencia = int(atributos[6])

               # Crear instancias de las subclases correspondientes
               if tipo == "GUE":
                    gato = entidades.Guerrero(nombre, vida_maxima, vida_maxima, poder, defensa, agilidad, resistencia)
               elif tipo == "MAG":
                    gato = entidades.Mago(nombre, vida_maxima, vida_maxima, poder, defensa, agilidad, resistencia)
               elif tipo == "CAB":
                    gato = entidades.Caballero(nombre, vida_maxima, vida_maxima, poder, defensa, agilidad, resistencia)

               gatos.append(gato)
     
     return gatos

def comprar_gato(opcion, dinero_disponible, ejercito):
     if opcion == 1:
          precio_gato = parametros.PRECIO_MAG
          tipo_gato = "MAG"
     elif opcion == 2:
          precio_gato = parametros.PRECIO_GUE
          tipo_gato = "GUE"
     elif opcion == 3:
          precio_gato = parametros.PRECIO_CAB
          tipo_gato = "CAB"

     if dinero_disponible < precio_gato:
          print("\n No tienes suficiente dinero para comprar este gato:( \n")
          return dinero_disponible
     
     nombre_tipo_gato = parametros.COMBATIENTES_BASICOS.get(tipo_gato)
     
     gatos_disponibles = cargar_unidad()

     # Filtrar gatos disponibles por tipo
     gatos_tipos = [gato for gato in gatos_disponibles if gato.tipo == nombre_tipo_gato]

     if not gatos_tipos:
          print(f"\n No hay gatos del tipo {nombre_tipo_gato} disponibles para comprar \n")
          return dinero_disponible

     # Se escoge de manera aleatoria un gato del tipo seleccionado
     gato_elegido = random.choice(gatos_tipos)

     #Se agrega el gato al ejercito
     ejercito.añadir_combatiente(gato_elegido)
     dinero_disponible -= precio_gato
     print(f"\n                Has comprado un gato tipo {nombre_tipo_gato}:) \n")
     return dinero_disponible

def aplicar_item(item, gato):
     
     if item == "Pergamino":
          if gato.tipo == "Guerrero":
               return entidades.Guerrero(gato._nombre, gato.vida_maxima, gato.vida, 
                                         gato.poder, gato.defensa, gato.agilidad, 
                                         gato.resistencia).evolucionar("Pergamino")
          elif gato.tipo == "Caballero":
               return entidades.Caballero(gato._nombre, gato.vida_maxima, gato._vida, 
                                         gato.poder, gato.defensa, gato.agilidad, 
                                         gato.resistencia).evolucionar("Pergamino")
     elif item == "Lanza":
          if gato.tipo == "Mago":
               return entidades.Mago(gato._nombre, gato.vida_maxima, gato.vida, 
                                         gato.poder, gato.defensa, gato.agilidad, 
                                         gato.resistencia).evolucionar("Lanza")
          elif gato.tipo == "Caballero":
               return entidades.Caballero(gato._nombre, gato.vida_maxima, gato.vida, 
                                         gato.poder, gato.defensa, gato.agilidad, 
                                         gato.resistencia).evolucionar("Lanza")               
    
     elif item == "Armadura":
          if gato.tipo == "Mago":
               return entidades.Mago(gato._nombre, gato.vida_maxima, gato.vida, 
                                         gato.poder, gato.defensa, gato.agilidad, 
                                         gato.resistencia).evolucionar("Armadura")
          elif gato.tipo == "Guerrero":
               return entidades.Guerrero(gato._nombre, gato.vida_maxima, gato.vida, 
                                         gato.poder, gato.defensa, gato.agilidad, 
                                         gato.resistencia).evolucionar("Armadura")                             

def comprar_item(opcion, dinero_disponible, ejercito):
     if opcion == 4:
          precio_item = parametros.PRECIO_ARMADURA
          tipo_item = "Armadura"
     
     elif opcion == 5:
          precio_item = parametros.PRECIO_PERGAMINO
          tipo_item = "Pergamino"
     
     elif opcion == 6:
          precio_item = parametros.PRECIO_LANZA
          tipo_item = "Lanza"

     if dinero_disponible < precio_item:
          print("\n      No tienes suficiente dinero para comprar el item \n")
          return dinero_disponible

     #Se verifica si hay gatos en el ejercito que puedan usar el item
     gatos_compatibles = [gato for gato in ejercito.combatientes if tipo_item in parametros.ITEMS_GATOS_COMPATIBLES.get(gato.tipo, [])]

     if not gatos_compatibles:
          print(f"\n       No hay gatos en tu ejercito que sean compatibles con el ítem \n")
          return dinero_disponible
     
     #Se despliega el menu de seleccion de gato
     seleccion = menus.selecciona_gato(gatos_compatibles, tipo_item)

     if seleccion == 0:
          return dinero_disponible
     
     gato_seleccionado = gatos_compatibles[seleccion - 1]
     nuevo_gato = aplicar_item(tipo_item, gato_seleccionado)

     if nuevo_gato:
          ejercito.eliminar_combatiente(gato_seleccionado)
          ejercito.añadir_combatiente(nuevo_gato)
          return dinero_disponible - precio_item

     else:
          return dinero_disponible

def curar_ejercito(dinero_disponible, ejercito):
     if dinero_disponible >= parametros.CURAR_VIDA * len(ejercito.combatientes):
          for combatiente in ejercito.combatientes:
               combatiente.curarse()
          dinero_disponible -= parametros.CURAR_VIDA * len(ejercito.combatientes)
          print(f"\nEl ejercito ha sido curado exitosamente")
     else:
          print("No tienes suficiente dinero para curar a tu ejercito")
     
     return dinero_disponible

def enfrentamiento(combatiente, enemigo):
     while combatiente.vida > 0 and enemigo.vida > 0:
               #Se realizan los ataques
               daño = combatiente.atacar(enemigo)
               combatiente.texto(daño, enemigo)

               daño_enemigo = enemigo.atacar(combatiente)
               enemigo.texto(daño_enemigo, combatiente)
               
               #Se efectúan los efectos de los ataques
               if combatiente.tipo in parametros.COMBATIENTES_BASICOS:
                    combatiente.efecto()
               if enemigo.tipo in parametros.COMBATIENTES_BASICOS:
                    enemigo.efecto()

               menus.txt_enfrentamiento(combatiente, enemigo)

               if combatiente.vida > 0 and enemigo.vida > 0:
                    daño_enemigo = enemigo.atacar(combatiente)
                    enemigo.texto(daño_enemigo, combatiente)

                    daño = combatiente.atacar(enemigo)
                    combatiente.texto(daño, enemigo)

                    #Se efectúan los efectos de los ataques
                    if combatiente.tipo in parametros.COMBATIENTES_BASICOS:
                         combatiente.efecto()
                    if enemigo.tipo in parametros.COMBATIENTES_BASICOS:
                         enemigo.efecto()
                    
                    menus.txt_enfrentamiento(combatiente, enemigo)

               elif combatiente.vida <= 0:
                    print(f"Gana {enemigo._nombre} este efrentamiento")
                    return combatiente
               elif enemigo.vida <= 0:
                    print(f"Gana {combatiente._nombre} este enfrentamiento")
                    return enemigo
               
     if combatiente.vida <= 0:
          print(f"Gana {enemigo._nombre} este efrentamiento")
          return combatiente
     
     elif enemigo.vida <= 0:
          print(f"Gana {combatiente._nombre} este enfrentamiento")
          return enemigo