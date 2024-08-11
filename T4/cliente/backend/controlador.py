import os
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from backend.ventana_inicio_back import Procesador
from backend.entidades import Puzzle, Tiempo, Pepa

class Controlador:
     def __init__(self):
          self.ventana_inicio = VentanaInicio()
          self.ventana_juego = None
          self.procesador = Procesador()
          self.tiempo = Tiempo()
          self.pepa = Pepa(0, 0, 0, 0)
          self.pepa_x = 0
          self.pepa_y = 0

          
          self.ventana_inicio.senal_comenzar.connect(self.abrir_ventana_juego)
          self.ventana_inicio.senal_verificar_usuario.connect(self.procesador.validar_usuario)
          self.procesador.senal_validacion_usuario.connect(self.ventana_inicio.validacion_usuario_resultado)

     def mover_pepa(self, direccion):
          if direccion == 'up':
               self.pepa_y -= 10
          elif direccion == 'down':
               self.pepa_y += 10
          elif direccion == 'left':
               self.pepa_x -= 10
          elif direccion == 'right':
               self.pepa_x += 10

          self.ventana_juego.actualizar_label_pepa(self.pepa_x, self.pepa_y)

     def abrir_ventana_juego(self, puzzle_seleccionado):
          self.ventana_inicio.hide()
          
          if self.ventana_juego and self.ventana_juego.isVisible():
               self.ventana_juego.close()
          
          self.ventana_juego = VentanaJuego()

          puzzle = self.obtener_tamano_puzzle(puzzle_seleccionado)
          puzzle.senal_mostrar_pepa.connect(self.ventana_juego.aparecer_pepa)
          self.ventana_juego.senal_teclas.connect(self.mover_pepa)
          self.ventana_juego.senal_volver_inicio.connect(self.abrir_ventana_inicio)
          self.ventana_juego.senal_pausar_juego.connect(self.tiempo.pausar_juego)
          self.tiempo.senal_actualizar_tiempo.connect(self.ventana_juego.actualizar_tiempo)

          self.pepa.senal_actualizar_pixmap.connect(self.ventana_juego.cambiar_pixmap)
          self.pepa.senal_mover_label.connect(self.ventana_juego.timer_mover_pepa.start)
          self.pepa.senal_mover_label.connect(self.ventana_juego.timer_animacion.start)
          self.pepa.senal_actualizar_label.connect(self.ventana_juego.actualizar_label_pepa)

          puzzle.crear_pepa()  # Asegúrate de que esto se llama
          self.ventana_juego.configurar_tablero(puzzle)
          self.ventana_juego.show()
          self.ventana_juego.tiempo.iniciar_juego()

     def abrir_ventana_inicio(self):
          if self.ventana_juego:
               self.ventana_juego.hide()
          self.ventana_inicio.show()

     def iniciar(self):
          self.ventana_inicio.show()

     def obtener_tamano_puzzle(self, puzzle):
          archivo = os.path.join('cliente', 'assets', 'base_puzzles', puzzle)
          return Puzzle.from_file(archivo)