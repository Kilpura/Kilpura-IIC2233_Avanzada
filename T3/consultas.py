from typing import Generator
from functools import reduce
from itertools import combinations
from utilidades import Animales, Candidatos, Distritos, Locales, Votos, Ponderador
import funciones

# ----------------------------------------------------------------------
# COMPLETAR
# ----------------------------------------------------------------------

# CARGA DE DATOS

def cargar_datos(tipo_generator: str, tamano: str):

    tipos_namedtuples = {
    "animales": Animales,
    "candidatos": Candidatos,
    "distritos": Distritos,
    "locales": Locales,
    "votos": Votos,
    "ponderadores": Ponderador
    }

    path_relativo = f"data\\{tamano}\\{tipo_generator}.csv"

    with open(path_relativo, 'r', encoding="latin-1") as file:
        next(file)

        tipo_de_namedtuple = tipos_namedtuples[tipo_generator]

        for linea in file:

            if tipo_generator == "locales":
                dato_limpio = funciones.limpiar_datos(linea)

            else:
                dato_limpio = funciones.str_a_int(linea)
            
            instancia_namedtuple = tipo_de_namedtuple(*dato_limpio)

            yield instancia_namedtuple

# 1 GENERADOR

def animales_segun_edad(generador_animales: Generator,
    comparador: str, edad: int) -> Generator:
    
    comparar_edad = {
        "<": lambda animal: int(animal.edad) < edad,
        ">": lambda animal: int(animal.edad) > edad,
        "=": lambda animal: int(animal.edad) == edad
    }

    funcion_comparadora = comparar_edad[comparador]

    animales_filtrados = filter(funcion_comparadora, generador_animales)

    for animal in animales_filtrados:
        yield animal.nombre

def animales_que_votaron_por(generador_votos: Generator,
    id_candidato: int) -> Generator:    
    
    for voto in generador_votos:
        if int(voto.id_candidato) == id_candidato:
            yield int(voto.id_animal_votante)

def cantidad_votos_candidato(generador_votos: Generator,
    id_candidato: int) -> int:
    
    return sum([1 for voto in generador_votos if int(voto.id_candidato) == id_candidato])

def ciudades_distritos(generador_distritos: Generator) -> Generator:
    
    provincias = set()
    
    for distrito in generador_distritos:
        provincias.add(distrito.provincia)
    
    yield from provincias


def especies_postulantes(generador_candidatos: Generator,
    postulantes: int) ->Generator:
    
    contador_especies = reduce(funciones.contar_especies, generador_candidatos, {})

    especies_filtradas = (especie for especie in contador_especies if contador_especies[especie] >= int(postulantes))

    yield from especies_filtradas


def pares_candidatos(generador_candidatos: Generator) -> Generator:

    # se generan todas las combinaciones de longitud 2 (pares)
    for candidato1, candidato2 in combinations(generador_candidatos, 2):
        yield (candidato1.nombre, candidato2.nombre)
        
def votos_alcalde_en_local(generador_votos: Generator, candidato: int,
    local: int) -> Generator:
    for voto in generador_votos:
        if int(voto.id_local) == local and int(voto.id_candidato) == candidato:
            yield voto

def locales_mas_votos_comuna (generador_locales: Generator,
    cantidad_minima_votantes: int, id_comuna: int) -> Generator:
    for local in generador_locales:
        if int(local.id_comuna) == int(id_comuna) and len(local.id_votantes) >= int(cantidad_minima_votantes):
            yield int(local.id_local)

def votos_candidato_mas_votado(generador_votos: Generator) -> Generator:

    votos_procesados = []
    conteo_votos = {}
    
    for voto in generador_votos:
        votos_procesados.append(voto)

        if voto.id_candidato in conteo_votos:
            conteo_votos[voto.id_candidato] += 1
        else:
            conteo_votos[voto.id_candidato] = 1

    max_votos = max(conteo_votos.values())

    candidatos = filter(lambda candidato: conteo_votos[candidato] == max_votos, conteo_votos.keys())

    candidatos_id = []
    for candidato in candidatos:
        candidato_id = candidato
        candidatos_id.append(candidato_id)

    candidato_mas_votado = max(candidatos_id)
    max_votos = conteo_votos[candidato_mas_votado]

    votos_filtrados = (voto for voto in votos_procesados if voto.id_candidato == candidato_mas_votado)

    for voto_filtrado in votos_filtrados:
        yield int(voto_filtrado.id_voto)
    
def animales_segun_edad_humana(generador_animales: Generator,
    generador_ponderadores: Generator, comparador: str,
    edad: int) -> Generator:

    pass

# 2 GENERADORES

def animal_mas_viejo_edad_humana(generador_animales: Generator,
    generador_ponderadores: Generator) -> Generator:
    # COMPLETAR
    pass


def votos_por_especie(generador_candidatos: Generator,
    generador_votos: Generator) -> Generator:
    # COMPLETAR
    pass


def hallar_region(generador_distritos: Generator,
    generador_locales: Generator, id_animal: int) -> str:
    # COMPLETAR
    pass


def max_locales_distrito(generador_distritos: Generator,
    generador_locales: Generator) -> Generator:
    # COMPLETAR
    pass


def votaron_por_si_mismos(generador_candidatos: Generator,
    generador_votos: Generator) -> Generator:
    # COMPLETAR
    pass


def ganadores_por_distrito(generador_candidatos: Generator,
    generador_votos: Generator) -> Generator:
    # COMPLETAR
    pass


# 3 o MAS GENERADORES

def mismo_mes_candidato(generador_animales: Generator,
    generador_candidatos: Generator, generador_votos: Generator,
    id_candidato: str) -> Generator:
    # COMPLETAR
    pass


def edad_promedio_humana_voto_comuna(generador_animales: Generator,
    generador_ponderadores: Generator, generador_votos: Generator,
    id_candidato: int, id_comuna:int ) -> float:
    # COMPLETAR
    pass


def votos_interespecie(generador_animales: Generator,
    generador_votos: Generator, generador_candidatos: Generator,
    misma_especie: bool = False,) -> Generator:
    # COMPLETAR
    pass


def porcentaje_apoyo_especie(generador_animales: Generator,
    generador_candidatos: Generator, generador_votos: Generator) -> Generator:
    # COMPLETAR
    pass


def votos_validos(generador_animales: Generator,
    generador_votos: Generator, generador_ponderadores) -> int:
    # COMPLETAR
    pass


def cantidad_votos_especie_entre_edades(generador_animales: Generator,
    generador_votos: Generator, generador_ponderador: Generator,
    especie: str, edad_minima: int, edad_maxima: int) -> str:
    # COMPLETAR
    pass


def distrito_mas_votos_especie_bisiesto(generador_animales: Generator,
    generador_votos: Generator, generador_distritos: Generator,
    especie: str) -> str:
    # COMPLETAR 
    pass


def votos_validos_local(generador_animales: Generator,
    generador_votos: Generator, generador_ponderadores: Generator,
    id_local: int) -> Generator:
    # COMPLETAR
    pass


def votantes_validos_por_distritos(generador_animales: Generator,
    generador_distritos: Generator, generador_locales: Generator,
    generador_votos: Generator, generador_ponderadores: Generator) -> Generator:
    # COMPLETAR
    pass