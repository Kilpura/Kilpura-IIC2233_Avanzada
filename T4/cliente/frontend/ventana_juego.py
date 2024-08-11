from PyQt6.QtCore import pyqtSignal, Qt, QTimer, QUrl
from PyQt6.QtGui import QPixmap
from PyQt6.QtMultimedia import QSoundEffect, QMediaPlayer, QAudioOutput
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from backend.entidades import Tiempo
from backend import parametros as p

class VentanaJuego(QWidget):
     senal_volver_inicio = pyqtSignal()
     senal_pausar_juego = pyqtSignal()
     senal_teclas = pyqtSignal(str)

     def __init__(self):
          super().__init__()
          self.label_pepa = None
          self.juego_pausado = False
          self.tiempo = Tiempo()
          self.tiempo.senal_actualizar_tiempo.connect(self.actualizar_tiempo)
          self.inicializa_gui()

          self.n_filas = 0
          self.n_columnas = 0
          self.celdas = {}
          self.celda_pepa = None
          self.lechugas = []
          
          self.sprite_index = 0
          self.timer_animacion = QTimer()
          self.timer_animacion.timeout.connect(self.cambiar_sprite)
          self.pixmaps_pepa = p.MOVIMIENTO_DOWN
          self.reproducir_sonido(p.MUSICA_2)

     def inicializa_gui(self):
          self.setWindowTitle("Ventana del Juego")
          self.setGeometry(300, 80, 900, 600)

          self.label_tiempo = QLabel('Tiempo Restante', self)
          self.label_tiempo_minutos = QLabel('00:00', self)

          layout_tiempo = QVBoxLayout()
          layout_tiempo.addWidget(self.label_tiempo)
          layout_tiempo.addWidget(self.label_tiempo_minutos)
          layout_tiempo.addStretch(1)

          self.boton_comprobar = QPushButton('Comprobar Solución', self)
          self.boton_comprobar.clicked.connect(self.comprobar_solucion)

          self.boton_pausar = QPushButton('Reanudar', self)
          self.boton_pausar.clicked.connect(self.pausar)

          self.boton_volver = QPushButton("Salir", self)
          self.boton_volver.clicked.connect(self.volver_inicio)

          layout_estadisticas = QVBoxLayout()
          layout_estadisticas.addStretch(1)
          layout_estadisticas.addLayout(layout_tiempo)
          layout_estadisticas.addStretch(1)
          layout_estadisticas.addWidget(self.boton_comprobar)
          layout_estadisticas.addStretch(1)
          layout_estadisticas.addWidget(self.boton_pausar)
          layout_estadisticas.addStretch(1)
          layout_estadisticas.addWidget(self.boton_volver)
          layout_estadisticas.addStretch(1)

          self.label_tablero = QGridLayout()
          self.label_tablero.setSpacing(0)
          self.widget_tablero = QWidget(self)
          self.widget_tablero.setLayout(self.label_tablero)

          self.labels_filas = []
          self.layouts_columnas = []

          layout_puzzle = QVBoxLayout()
          layout_puzzle.addWidget(self.widget_tablero)

          layout_principal = QHBoxLayout()
          layout_principal.addLayout(layout_puzzle)
          layout_principal.addLayout(layout_estadisticas)
          layout_principal.addStretch(1)

          self.setStyleSheet("""
               background-color: #D4E6F1;
               color: black;
               font-size: 13pt;
          """)

          self.setLayout(layout_principal)

          self.timer_mover_pepa = QTimer(self)
          self.timer_mover_pepa.setInterval(10)
          self.timer_mover_pepa.timeout.connect(self.mover_pepa) #

          self.timer_animacion = QTimer(self)
          self.timer_animacion.setInterval(30)
          self.timer_animacion.timeout.connect(self.cambiar_pixmap)

          self.imagen_actual_pepa = 0
          self.pixmaps_pepa = []

     def reproducir_sonido(self, ruta_sonido):
          efecto_sonido = QSoundEffect(self)
          efecto_sonido.setVolume(5)
          url = QUrl.fromLocalFile(ruta_sonido)
          efecto_sonido.setSource(url)

          efecto_sonido.play()

     def aparecer_pepa(self, x, y):

          self.pepa_x = x
          self.pepa_y = y

          if not self.label_pepa:

               self.label_pepa = QLabel(self)
               
               self.label_pepa.setGeometry(x+19, y+19, 30, 30)
               self.label_pepa.setPixmap(QPixmap(p.POSICION_INICIAL))
               self.label_pepa.setScaledContents(True)
               self.label_pepa.setStyleSheet("background: transparent;")
               self.label_pepa.show()

     def keyPressEvent(self, event):
          if event.key() == Qt.Key.Key_W and not event.isAutoRepeat():
               self.pixmaps_pepa = p.MOVIMIENTO_UP
               self.mover_pepa(0, -1)
          elif event.key() == Qt.Key.Key_S and not event.isAutoRepeat():
               self.pixmaps_pepa = p.MOVIMIENTO_DOWN
               self.mover_pepa(0, 1)
          elif event.key() == Qt.Key.Key_A and not event.isAutoRepeat():
               self.pixmaps_pepa = p.MOVIMIENTO_LEFT
               self.mover_pepa(-1, 0)
          elif event.key() == Qt.Key.Key_D and not event.isAutoRepeat():
               self.pixmaps_pepa = p.MOVIMIENTO_RIGHT
               self.mover_pepa(1, 0)
          elif event.key() == Qt.Key.Key_G and not event.isAutoRepeat():
               self.comer_lechuga()
     
     def comer_lechuga(self):
          fila, columna = self.pepa_y, self.pepa_x  # Ajustar según la lógica de tu juego
          if (fila, columna) in self.celdas:
               celda = self.celdas[(fila, columna)]
               pixmap_lechuga = QPixmap(p.LECHUGA)
               if celda.pixmap().toImage().cacheKey() == pixmap_lechuga.toImage().cacheKey():
                    celda.clear()
                    self.reproducir_sonido(p.COMER)
               else:
                    celda.setPixmap(QPixmap(p.POOP))
                    self.reproducir_sonido(p.SONIDO_POOP)
                    QTimer.singleShot(p.TIEMPO_TRANSICION * 1000, lambda: celda.setPixmap(QPixmap(p.LECHUGA)))

     def restaurar_lechuga(self, celda):
          # Restaurar lechuga después del tiempo de transición
          celda.setPixmap(QPixmap(p.LECHUGA))


     def lista_pixmap(self, lista_pixmap):
          self.pixmaps_pepa = lista_pixmap

     def cambiar_pixmap(self):
          pixmap_nuevo = self.pixmaps_pepa[self.imagen_actual_pepa]
          self.label_pepa.setPixmap(pixmap_nuevo)
          self.imagen_actual_pepa += 1
          if self.imagen_actual_pepa == 3:
               self.imagen_actual_pepa = 0

     def mover_pepa(self, dx, dy):

          nuevo_x = self.pepa_x + dx
          nuevo_y = self.pepa_y + dy

          if 0 <= nuevo_x < self.n_columnas and 0 <= nuevo_y < self.n_filas:
               self.pepa_x = nuevo_x
               self.pepa_y = nuevo_y
               self.animar_movimiento()
     
     def animar_movimiento(self):
          self.sprite_index = 0
          self.timer_animacion.start(100)
          self.actualizar_posicion_pepa()
     
     def cambiar_sprite(self):
          pixmap_nuevo = self.pixmaps_pepa[self.sprite_index]
          self.label_pepa.setPixmap(QPixmap(pixmap_nuevo))
          self.sprite_index = (self.sprite_index + 1) % len(self.pixmaps_pepa)

          if self.sprite_index == 0:
               self.timer_animacion.stop()
     
     def actualizar_posicion_pepa(self):
          tamano_celda = min(600 // self.n_filas, 600 // self.n_columnas)
          pos_x = self.pepa_x * tamano_celda + 19  # Ajusta los valores (19, 19) según sea necesario
          pos_y = self.pepa_y * tamano_celda + 19
          self.label_pepa.setGeometry(pos_x, pos_y, tamano_celda, tamano_celda)
          
     def actualizar_label_pepa(self, x, y):
          self.pepa_x = x
          self.pepa_y = y

     def levantar(self):
          self.label_pepa.raise_()      #no se q hace aun

     def configurar_tablero(self, puzzle):
          self.n_filas = len(puzzle.filas)
          self.n_columnas = len(puzzle.columnas)
          tamano_celda = min(600 // self.n_filas, 600 // self.n_columnas)

          # Limpiar cualquier widget previo en el layout de tablero
          for i in reversed(range(self.label_tablero.count())):
               widget = self.label_tablero.itemAt(i).widget()
               if widget is not None:
                    self.label_tablero.removeWidget(widget)
                    widget.deleteLater()

          self.celdas = {}  # Reiniciar el diccionario de celdas

          # Agregar etiquetas de filas
          for i in range(self.n_filas):
               label_fila = QLabel("", self)
               label_fila.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
               if puzzle.filas[i]:
                    texto_fila = ' '.join(map(str, puzzle.filas[i]))
               else:
                    texto_fila = '-'
               label_fila.setText(texto_fila)
               self.labels_filas.append(label_fila)
               self.label_tablero.addWidget(label_fila, i, self.n_columnas, 1, 1)

          # Agregar etiquetas de columnas
          for j in range(self.n_columnas):
               layout_columna = QVBoxLayout()  # QVBoxLayout para la columna j
               for numero in puzzle.columnas[j]:
                    label_columna = QLabel(str(numero), self)
                    label_columna.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    layout_columna.addWidget(label_columna)
               self.layouts_columnas.append(layout_columna)
               layout_columna.addStretch(1)
               self.label_tablero.addLayout(layout_columna, self.n_filas, j)

          # Agregar celdas del tablero
          for i in range(self.n_filas):
               for j in range(self.n_columnas):
                    celda = QLabel("", self)
                    celda.setFixedSize(tamano_celda, tamano_celda)
                    celda.setPixmap(QPixmap(p.LECHUGA))
                    celda.setScaledContents(True)
                    celda.setStyleSheet("border: 1px solid black;")
                    self.label_tablero.addWidget(celda, i, j)
                    self.celdas[(i, j)] = celda  # Agregar la celda al diccionario de celdas

     def actualizar_tiempo(self, tiempo):
          self.label_tiempo_minutos.setText(tiempo)

     def volver_inicio(self):
          self.senal_volver_inicio.emit()

     def pausar(self):
          self.juego_pausado = not self.juego_pausado
          if self.juego_pausado:
               self.boton_pausar.setText('Reanudar')
               self.widget_tablero.hide()
               self.label_pepa.hide()
          else:
               self.boton_pausar.setText('Pausar')
               self.widget_tablero.show()
               self.label_pepa.show()
               
          self.tiempo.pausar_juego()

     def mostrar_ventana(self):
          self.show()

     def comprobar_solucion(self):
          pass