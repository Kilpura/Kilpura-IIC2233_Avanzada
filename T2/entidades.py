from abc import ABC, abstractmethod
import parametros
import random
import menus
import funciones

class Ejercito:

     def __init__(self, combatientes, **kwargs):
          super().__init__(**kwargs)
          self.combatientes = combatientes
          self.oro = 0
     
     def combatir(self, ejercito_enemigo):

          while 0 < len(self.combatientes) and 0 < len(ejercito_enemigo.combatientes):
               for combatiente in self.combatientes:
                    for enemigo in ejercito_enemigo.combatientes:

                         print(f"\n*** Enfrentamiento entre {combatiente._nombre} y {enemigo._nombre} ***")
                         print(combatiente)
                         print(enemigo)

                         perdedor = funciones.enfrentamiento(combatiente, enemigo)

                         if perdedor and perdedor in self.combatientes:
                              self.eliminar_combatiente(perdedor)
                              print(f"{perdedor._nombre} ha sido eliminado del ejército")

                         elif perdedor and perdedor in ejercito_enemigo.combatientes:
                              ejercito_enemigo.eliminar_combatiente(perdedor)
                              print(f"{perdedor._nombre} ha sido eliminado del ejército enemigo")

          if len(self.combatientes) == 0 and len(ejercito_enemigo.combatientes) == 0:
               print("\nEmpate :p")
               return False
          
          elif len(ejercito_enemigo.combatientes) == 0:
               print("\nEquipo enemigo derrotado >:)")
               return True
          
          elif len(self.combatientes) == 0:
               print("\nPerdiste, no te quedan más gatitos")
               return False

     def __str__(self):

          ejercito_str = "                 *** Este es tu Ejército Actual ***\n"

          for combatiente in self.combatientes:
               ejercito_str += f"\n Holaa! mi nombre es {combatiente._nombre}, " + \
                    f"soy un {combatiente.tipo} con {combatiente.vida} de vida, " + \
                    f"{round(combatiente.ataque, 2)} de ataque y {round(combatiente.defensa, 2)} de defensa"

          ejercito_str += f"\n Actualmente tienes {len(self.combatientes)} gatitos combatientes." + \
               f"¡Éxito, Guerrero:)!"
          
          return ejercito_str
     
     # Método añadido
     def añadir_combatiente(self, nuevo_combatiente):
          self.combatientes.append(nuevo_combatiente)
     
     # Método añadido
     def eliminar_combatiente(self, combatiente):
          self.combatientes.remove(combatiente)

class Combatiente:

     def __init__(self, nombre, vida_maxima, vida, poder, defensa, 
                  agilidad, resistencia, **kwargs):
          super().__init__(**kwargs)
          self._nombre = nombre
          self._vida_maxima = vida_maxima
          self._vida = vida
          self._poder = poder
          self._defensa = defensa
          self._agilidad = agilidad
          self._resistencia = resistencia
          self.tipo = ""

     # Vida Máxima debe tener un valor entre 0 y 100
     @property
     def vida_maxima(self):
          return self._vida_maxima
     
     @vida_maxima.setter
     def vida_maxima(self, valor):
          if 0 <= valor <= 100:
               self._vida_maxima = valor
          elif valor < 0:
               self._vida_maxima = 0
          else:
               self._vida_maxima = 100
     
     # Vida debe ser un número entre 0 y Vida Maxima
     @property
     def vida(self):
          return self._vida
     
     @vida.setter
     def vida(self, valor):
          if 0 <= valor <= self._vida_maxima:
               self._vida = valor
          elif valor < 0:
               self._vida = 0
          else:
               self._vida = self._vida_maxima

     # Poder debe ser un valor entre 1 y 10
     @property
     def poder(self):
          return self._poder
     
     @poder.setter
     def poder(self, valor):
          if 0 <= valor <= 10:
               self._poder = valor
          elif valor < 0:
               self._poder = 0
          else:
               self._poder = 10
     
     # Defensa debe ser un valor entre 1 y 20
     @property
     def defensa(self):
          return self._defensa

     @defensa.setter
     def defensa(self, valor):
          if 1 <= valor <= 20:
               self._defensa = valor
          elif valor < 1:
               self._defensa = 1
          else:
               self._defensa = 20
     
     # Agilidad debe ser un valor entre 1 y 10
     @property
     def agilidad(self):
          return self._agilidad
     
     @agilidad.setter
     def agilidad(self, valor):
          if 1 <= valor <= 10:
               self._agilidad = valor
          elif valor < 1:
               self._agilidad = 1
          else:
               self._agilidad = 10
     
     # Resistencia debe ser un valor entre 1 y 10
     @property
     def resistencia(self):
          return self._resistencia
     
     @resistencia.setter
     def resistencia(self, valor):
          if 1 <= valor <= 10:
               self._resistencia = valor
          elif valor < 1:
               self._resistencia = 1
          else:
               self._resistencia = 10

     @property
     def ataque(self):
          parte_1 = self.poder + self.agilidad + self.resistencia
          parte_2 = (2 * self.vida) / self.vida_maxima

          return int(round(parte_1 * parte_2))
     
     @abstractmethod
     def atacar(self, enemigo):
          pass
     
     @abstractmethod
     def evolucionar(self, item):
          pass
     
     def curarse(self):
          self.vida = min(self.vida + parametros.CURAR_VIDA, self.vida_maxima)

     def __str__(self):
          texto = f"""
          Mi nombre es {self._nombre} y actualmente mis características son:
          Vida = {self.vida} / {self.vida_maxima}
          Poder = {round(self.ataque, 2)}
          Defensa = {round(self.defensa, 2)}
          Tipo = {self.tipo}"""
          return texto

class Itemes:

     def __init__(self, nombre, descripcion):
          self.nombre = nombre
          self.descripcion = descripcion

     def describir(self):
          return f"{self.nombre}: {self.descripcion}"
     
class Guerrero(Combatiente):

     def __init__(self, nombre, vida_maxima, vida, poder, defensa, agilidad, resistencia):
          super().__init__(nombre, vida_maxima, vida, poder, defensa, agilidad, resistencia)
          self.tipo = "Guerrero"

     def texto(self, daño, enemigo):
          print(f"\n          Guerrero {self._nombre} ataca a {enemigo._nombre} con " +
               f"{daño} de daño.")

     def atacar(self, enemigo):
          daño = round(self.ataque - enemigo.defensa)

          # Se garantiza que el daño sea mayor o igual a 1
          daño = max(1, daño)
          enemigo.vida -= daño
          return daño

     #Método añadido 
     def efecto(self):
          self.agilidad -= self.agilidad * parametros.CANSANCIO / 100

     def evolucionar(self, item):
          if item == "Pergamino":
               print(f"\n{self._nombre} ha evolucionado a Mago de Batalla")
               return MagoBatalla(self._nombre, self.vida_maxima, self.vida, self.poder, 
                                  self.defensa, self.agilidad, self.resistencia)
               
          elif item == "Armadura":
               print(f"\n{self._nombre} ha evolucionado a Paladín")
               return Paladin(self._nombre, self.vida_maxima, self.vida, self.poder, 
                              self.defensa, self.agilidad, self.resistencia)

class Caballero(Combatiente):

     def __init__(self, nombre, vida_maxima, vida, poder, defensa, agilidad, resistencia):
          super().__init__(nombre, vida_maxima, vida, poder, defensa, agilidad, resistencia)
          self.tipo = "Caballero"

     def texto(self, daño, enemigo):
          print(f"\n          Caballero {self._nombre} ataca a {enemigo._nombre} con " +
               f"{daño} de daño.")

     def atacar(self, enemigo):

          if random.randint(1, 100) <= parametros.PROB_CAB:
               #Se reduce el Poder del enemigo en un red_cab%
               enemigo.poder = enemigo.poder - (enemigo.poder * (parametros.RED_CAB / 100))
               #Luego ataca con un atq_cab% de su ataque
               daño = round(self.ataque * (parametros.ATQ_CAB / 100) - enemigo.defensa)
          
          else:
               #Ataca igual como un guerrero
               daño = round(self.ataque - enemigo.defensa)
          
          daño = max(1, daño)
          enemigo.vida -= daño 
          return daño

     #Método añadido
     def efecto(self):
          self.resistencia -= self.resistencia * parametros.CANSANCIO / 100

     def evolucionar(self, item):
          if item == "Pergamino":
               print(f"\n{self._nombre} ha evolucionado a Caballero Arcano")
               return CaballeroArcano(self._nombre, self.vida_maxima, self.vida, self.poder, 
                                      self.defensa, self.agilidad, self.resistencia)
               
          elif item == "Lanza":
               print(f"\n{self._nombre} ha evolucionado a Paladín")
               return Paladin(self._nombre, self.vida_maxima, self.vida, self.poder, 
                              self.defensa, self.agilidad, self.resistencia)

class Mago(Combatiente):

     def __init__(self, nombre, vida_maxima, vida, poder, defensa, agilidad, resistencia):
          super().__init__(nombre, vida_maxima, vida, poder, defensa, agilidad, resistencia)
          self.tipo = "Mago"
     
     def texto(self, daño, enemigo):
          print(f"\n          Mago {self._nombre} ataca a {enemigo._nombre} con " + 
               f"{daño} de daño.")

     def atacar(self, enemigo):

          if random.randint(1, 100) <= parametros.PROB_MAG:
               #Se reduce la Defensa del enemigo en un red_mag%
               enemigo.defensa = enemigo.defensa - (enemigo.defensa * (parametros.RED_MAG / 100))
               #Luego ataca con un atq_mag% de su ataque
               daño = round(self.ataque * (parametros.ATQ_MAG / 100) - 
                            enemigo.defensa * (100 - parametros.RED_MAG) / 100) 
          else:
               #Ataca igual como un guerrero
               daño = round(self.ataque - enemigo.defensa)
          
          # Se garantiza que el daño sea mayor o igual a 1
          daño = max(1, daño)
          enemigo.vida -= daño
          return daño

     #Método añadido
     def efecto(self):
          self.agilidad -= self.agilidad * parametros.CANSANCIO / 100
          self.resistencia -= (self.resistencia * parametros.CANSANCIO / 100)

     def evolucionar(self, item):
          if item == "Lanza":
               print(f"\n{self._nombre} ha evolucionado a Mago de Batalla")
               return MagoBatalla(self._nombre, self.vida_maxima, self.vida, self.poder, 
                                  self.defensa, self.agilidad, self.resistencia)
               
          elif item == "Armadura":
               print(f"\n{self._nombre} ha evolucionado a Caballero Arcano")
               return CaballeroArcano(self._nombre, self.vida_maxima, self.vida, self.poder,
                                       self.defensa, self.agilidad, self.resistencia)

class Paladin(Caballero, Guerrero):

     def __init__(self, nombre, vida_maxima, vida, poder, defensa, agilidad, resistencia):
          super().__init__(nombre, vida_maxima, vida, poder, defensa, agilidad, resistencia)
          self.tipo = "Paladin"

     def texto(self, daño, enemigo):
          print(f"\n          Paladín {self._nombre} ataca a {enemigo._nombre} con " +
               f"{daño} de daño.")

     def atacar(self, enemigo):
          if random.randint(1, 100) <= parametros.PROB_PAL:
               #Se activan los poderes de caballero
               daño = Caballero.atacar(self, enemigo)
          
          else:
               #Se activan los poderes de guerrero
               daño = Guerrero.atacar(self, enemigo)
     
          #Efecto del paladín
          self.resistencia += parametros.AUM_PAL / 100
          return daño
     
class MagoBatalla(Mago, Guerrero):

     def __init__(self, nombre, vida_maxima, vida, poder, defensa, agilidad, resistencia):
          super().__init__(nombre, vida_maxima, vida, poder, defensa, agilidad, resistencia)
          self.tipo = "Mago de Batalla"

     def texto(self, daño, enemigo):
          print(f"\n          Mago de Batalla {self._nombre} ataca a {enemigo._nombre} con " +
                 f"{daño} de daño.")

     def atacar(self, enemigo):
          if random.randint(1, 100) <= parametros.PROB_MDB:
               #Se activan los poderes de mago
               daño = Mago.atacar(self, enemigo)          
          else:
               #Se activan los poderes de guerrero
               daño = Guerrero.atacar(self, enemigo)
          #Efecto del Mago de batalla
          self.agilidad -= parametros.CANSANCIO / 100
          self.defensa += parametros.DEF_MDB / 100
          return daño
     
class CaballeroArcano(Caballero, Mago):

     def __init__(self, nombre, vida_maxima, vida, poder, defensa, agilidad, resistencia):
          super().__init__(nombre, vida_maxima, vida, poder, defensa, agilidad, resistencia)
          self.tipo = "Caballero Arcano"
     
     def texto(self, daño, enemigo):
          print(f"\n          Caballero Arcano {self._nombre} ataca a {enemigo._nombre} con " +
               f"{daño} de daño.")

     def atacar(self, enemigo):
          if random.randint(1, 100) <= parametros.PROB_CAR:
               #Se activan los poderes de caballero
               daño = Caballero.atacar(self, enemigo)          
          else:
               #Se activan los poderes de Mago
               daño = Mago.atacar(self, enemigo)

          #Efecto del Caballero arcano
          self.poder += parametros.AUM_CAR / 100
          self.agilidad += parametros.AUM_CAR / 100
          self.resistencia -= parametros.CANSANCIO / 100
          return daño