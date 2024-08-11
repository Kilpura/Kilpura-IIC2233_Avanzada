import os

PORT_DEFECTO = 4444

HOST_DEFECTO = "localhost"

SIZE_BUFFER = 4096

TIEMPO_JUEGO = 300
"""
300 segundos de juego
"""
TIEMPO_ADICIONAL = 30
"""
30 segundos adicionales
"""
CONSTANTE = 100

TIEMPO_APARICION = 20

TIEMPO_DURACION = 5

TIEMPO_TRANSICION = 10

POSICION_INICIAL = os.path.join('cliente', 'assets', 'sprites', 'pepa', 'down_0.png')

MOVIMIENTO_RIGHT = [
    os.path.join('cliente', 'assets', 'sprites', 'pepa', 'right_0.png'),
    os.path.join('cliente', 'assets', 'sprites', 'pepa', 'right_1.png'),
    os.path.join('cliente', 'assets', 'sprites', 'pepa', 'right_2.png'),
    os.path.join('cliente', 'assets', 'sprites', 'pepa', 'right_3.png')
]

MOVIMIENTO_DOWN = [
    os.path.join('cliente', 'assets', 'sprites', 'pepa', 'down_0.png'),
    os.path.join('cliente', 'assets', 'sprites', 'pepa', 'down_1.png'),
    os.path.join('cliente', 'assets', 'sprites', 'pepa', 'down_2.png'),
    os.path.join('cliente', 'assets', 'sprites', 'pepa', 'down_3.png')
]

MOVIMIENTO_UP = [
    os.path.join('cliente', 'assets', 'sprites', 'pepa', 'up_0.png'),
    os.path.join('cliente', 'assets', 'sprites', 'pepa', 'up_1.png'),
    os.path.join('cliente', 'assets', 'sprites', 'pepa', 'up_2.png'),
    os.path.join('cliente', 'assets', 'sprites', 'pepa', 'up_3.png')
]

MOVIMIENTO_LEFT = [
    os.path.join('cliente', 'assets', 'sprites', 'pepa', 'left_0.png'),
    os.path.join('cliente', 'assets', 'sprites', 'pepa', 'left_1.png'),
    os.path.join('cliente', 'assets', 'sprites', 'pepa', 'left_2.png'),
    os.path.join('cliente', 'assets', 'sprites', 'pepa', 'left_3.png')
]

LECHUGA = os.path.join('cliente', 'assets', 'sprites', 'lechuga.png')

POOP = os.path.join('cliente', 'assets', 'sprites', 'poop.png')

SANDIA = os.path.join('cliente', 'assets', 'sprites', 'sandia.png')

COMER = os.path.join('cliente', 'assets', 'sonidos', 'comer.wav')

JUEGO_GANADO = os.path.join('cliente', 'assets', 'sonidos', 'juego_ganado.wav')

JUEGO_PERIDO = os.path.join('cliente', 'assets', 'sonidos', 'juego_perdido.wav')

MUSICA_1 = os.path.join('cliente', 'assets', 'sonidos', 'musica_1.wav')

MUSICA_2 = os.path.join('cliente', 'assets', 'sonidos', 'musica_2.wav')

OBTENER_SANDIA = os.path.join('cliente', 'assets', 'sonidos', 'obtener_sandia.wav')

SONIDO_POOP = os.path.join('cliente', 'assets', 'sonidos', 'poop.wav')