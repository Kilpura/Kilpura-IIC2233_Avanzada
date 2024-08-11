from typing import Generator
from utilidades import Animales, Candidatos, Distritos, Locales, Votos, Ponderador
from functools import reduce

def limpiar_datos(dato):
     datos_limpios = []
     dato_actual = ''
     dentro_corchetes = False

     for char in dato.strip():
          if char == '[':
               dentro_corchetes = True
          elif char == ']':
               dentro_corchetes = False
          elif char == ',' and not dentro_corchetes:
               datos_limpios.append(dato_actual.strip())
               dato_actual = ''
          else:
               dato_actual += char
     
     # Agregar el último dato
     datos_limpios.append(dato_actual.strip())

     # Obtener la lista de números del último dato y convertirlos a enteros
     lista = datos_limpios[-1]
     numeros_str = lista.split(",")

     numeros = [int(elemento) for elemento in numeros_str if elemento.strip().isdigit()]

     # Reemplazar el último dato en datos_limpios con la lista de números
     datos_limpios[-1] = numeros

     return datos_limpios

def str_a_int(dato):
     dato = dato.strip().split(",")

     dato_limpios = [int(elemento) if elemento.isdigit() else elemento for elemento in dato]

     return dato_limpios

def contar_especies(contador: dict, candidato: isinstance):
     """
     Args:
          contador: Mantiene el recuento de cada especie encontrada
          candidato: Instancia de Candidatos
     Returns:
          contador actualizado
     """
     #BUSCARLOOOOOOOOOOOO
     especie = candidato.especie
     contador[especie] = contador.get(especie, 0) + 1
     return contador

def contar_votos(contador, voto):
     candidato = voto.id_candidato
     if candidato in contador:
          contador[candidato] += 1
     else:
          contador[candidato] = 1

     return contador
