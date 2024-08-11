RUTA_FACIL = "data/facil.txt"
RUTA_INTERMEDIO = "data/intermedio.txt"
RUTA_DIFICIL = "data/dificil.txt"
RUTA_PRUEBA = "data/prueba.txt"
RUTAS_DIFICULTAD = {
    "facil": RUTA_FACIL,
    "intermedio": RUTA_INTERMEDIO,
    "dificil": RUTA_DIFICIL,
    "prueba": RUTA_PRUEBA
}

TIPOS_COMBATIENTES = {
    'MAG': 'Mago',
    'CAB': 'Caballero',
    'GUE': 'Guerrero',
    'CAR': 'Cazador',
    'PAL': 'Paladín',
    'MDB': 'Médico'
}

COMBATIENTES_BASICOS = {
    'MAG': 'Mago',
    'CAB': 'Caballero',
    'GUE': 'Guerrero'
}

ITEMS_GATOS_COMPATIBLES = {
        "Guerrero": ["Armadura", "Pergamino"],
        "Mago": ["Lanza", "Armadura"],
        "Caballero": ["Pergamino", "Lanza"]
}

ORO_INICIAL = 100 
"""
Se cuenta con oro con el cual se pueden comprar artículos en la Tienda
"""
ORO_GANADO = 50
"""
Dinero obtenido si se consigue ganar la ronda
"""

# Precios para el Menú de Tienda
PRECIO_MAG = 20
"""
Precio de un combatiente de tipo Mago
"""
PRECIO_GUE = 15
"""
Precio de un combatiente de tipo Guerrero
"""
PRECIO_CAB = 30
"""
Precio de un combatiente de tipo Caballero
"""

PRECIO_ARMADURA = 15
"""
Precio del Ítem Armadura

Armadura:
     Permite evolucionar a un Mago o Guerrero en un Caballero Arcano o Paladín
     ***********NO SE PUEDE SER USADO EN UN CABALLERO***********
"""
PRECIO_PERGAMINO = 10
"""
Precio del Ítem Pergamino

Pergamino: 
     Permite evolucionar a un Guerrero o Caballero en un Mago de Batalla o un Caballero Arcano
     **********NO PUEDE SER USADO EN UN MAGO*************
"""
PRECIO_LANZA = 15
"""
Precio del Ítem Lanza 

Lanza:
     Permite evolucionar a un Mago o Caballero en un Mago de Batalla o Paladín
     *********NO SE PUEDE USAR EN UN GUERRERO******
"""

PRECIO_CURA = 40    
"""
Precio de la opción Curar Ejército
"""

CURAR_VIDA = 20
"""
Cantidad de "vida" obtenida de la opción Curar ejercito
"""

CANSANCIO = 30
"""
En cada ataque, se disminuye en un 20%:
Guerrero: La Agilidad
Caballero: La Resistencia
Mago: La Resistencia y Agilidad
Mago de Batalla: La Agilidad
Caballero Arcano: La Resistencia
"""

"""
CABALLERO
     Su habilidad especial es de sorprender a su rival y reducir su Poder
"""
PROB_CAB = 50
"""
El Caballero tiene un 50% de probabilidad de activar su habilidad
"""
RED_CAB = 20
"""
Si la habilidad es activada, se reduce el Poder del rival en un 20%
"""
ATQ_CAB = 80
"""
Luego de activar su habilidad, el Caballero ataca con un 80% de su ataque original
"""

"""
MAGO
     Su habilidad especial es de reducir la Defensa del rival
"""
PROB_MAG = 55
"""
El Mago tiene un 55% de probabilidad de activar su habilidad 
"""
RED_MAG = 60
"""
Si la habilidad es activada, se reduce la Defensa del rival un 60%
"""
ATQ_MAG = 80
"""
Luego de activar su habilidad, el Mago ataca con un 80% de su ataque original
"""

"""
PALADÍN
     Su habilidad especial es la de un Caballero.
     Sorprender a su rival y reducir su Poder.
"""
PROB_PAL = 50
"""
El Paladín tiene un 50% de probabilidad de activar su habilidad
"""
AUM_PAL = 5
"""
Luego de cada ataque, su Resistencia aumenta un 5%
"""

"""
MAGO DE BATALLA
     Su habilidad especial es la de un Mago.
     Reduce la Defensa del rival.
"""
PROB_MDB = 40
"""
El Mago de Batalla tiene un 40% de probabilidad de activar su habilidad
"""
DEF_MDB = 5
"""
Luego de cada ataque, su Defensa aumenta en un 5%
"""

"""
CABALLERO ARCANO
     Su habilidad especial es la de un Caballero o un Mago.
     Caballero: Sorprender a su rival y reducir su Poder
     Mago: Reducir la Defensa de su rival
"""
PROB_CAR = 40
"""
El Caballero Arcano tiene un 40% de probabilidad de activar su habilidad de Caballero
"""
PROB_CAR_MAG = 100 - PROB_CAR
"""
El Caballero Arcano tiene un 60% de probabilidad de activar su habilidad de Mago
"""
AUM_CAR = 3
"""
El Caballero Arcano aumenta en un 3% su Poder y Agilidad
"""