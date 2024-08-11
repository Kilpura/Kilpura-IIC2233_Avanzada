from backend import parametros as p
from PyQt6.QtCore import pyqtSignal, QTimer, QObject
from PyQt6.QtGui import QPixmap

class Pepa(QObject):
     senal_actualizar_pixmap = pyqtSignal(list)
     senal_actualizar_label = pyqtSignal(int, int)
     senal_mover_label = pyqtSignal()

     def __init__(self, x, y, fila, columna):
          super().__init__()
          self.__x = x
          self.__y = y
          self.fila = fila
          self.columna = columna
          self.direcciones = {'up': (0, -36), 'down': (0, 36),
                              'left': (-39, 0), 'right': (39, 0)}
          self.crear_pixmaps()
     
     @property
     def x(self) -> int:
          return self.__x

     @x.setter
     def x(self, p: int) -> None:
          if p < 500:
               self.__x = 500
          elif p > 810:
               self.__x = 810
          else:
               self.__x = p

     @property
     def y(self) -> int:
          return self.__y

     @y.setter
     def y(self, p: int) -> None:
          if p < 49:
               self.__y = 49
          elif p > 515:
               self.__y = 515
          else:
               self.__y = p     

     def crear_pixmaps(self):
          self.pepa_up = []
          self.pepa_down = []
          self.pepa_left = []
          self.pepa_right = []

          for i in range(3):
               pixmap_up = QPixmap(p.MOVIMIENTO_UP[i])
               pixmap_down = QPixmap(p.MOVIMIENTO_DOWN[i])
               pixmap_left = QPixmap(p.MOVIMIENTO_LEFT[i])
               pixmap_right = QPixmap(p.MOVIMIENTO_RIGHT[i])
               self.pepa_up.append(pixmap_up)
               self.pepa_down.append(pixmap_down)
               self.pepa_left.append(pixmap_left)
               self.pepa_right.append(pixmap_right)
          self.pixmap_direccion = {'up': self.pepa_up,
                                   'down': self.pepa_down,
                                   'left': self.pepa_left,
                                   'right': self.pepa_right}

     def mover_pepa(self, direccion):
          incremento = self.direcciones[direccion]
          self.senal_actualizar_pixmap.emit(self.pixmap_direccion[direccion])
          self.x += incremento[0]
          self.y += incremento[1]
          self.senal_actualizar_label.emit(self.x, self.y)
          self.senal_mover_label.emit()
     
     def comer_lechuga(self, x, y, signal_actualizar_label):
          # Aquí se marca la casilla como vacía y se emite la señal para actualizar la GUI
          # Suponiendo que el tablero es una matriz 2D donde (x, y) es la posición
          self.x = x
          self.y = y
          self.senal_actualizar_label.emit(self.x, self.y)
     
     def hacer_poop(self, x, y, signal_actualizar_label):
          # Aquí se genera la popó en la casilla vacía y se emite la señal para actualizar la GUI
          # Suponiendo que el tablero es una matriz 2D donde (x, y) es la posición
          self.x = x
          self.y = y
          self.senal_actualizar_label.emit(self.x, self.y)

class Puzzle(QObject):
     senal_mostrar_ventana = pyqtSignal()
     senal_mostrar_pepa = pyqtSignal(int, int)
     
     def __init__(self, n:int, filas:list, columnas:list):
          """
          n: Dimensión del puzzle nxn
          filas: Lista de listas con los números de cada fila
          columna: Lista de listas con los números de cada columna
          """
          super().__init__()
          self.n = n
          self.filas = filas
          self.columnas = columnas
          self.tablero = [[1 for _ in range(n)] for _ in range(n)]
          self.crear_pepa()
     
     def imprimir_tablero(self):
          for fila in self.tablero:
               print(fila)

     def crear_pepa(self):
          self.pepa = Pepa(0, 0, 0, 0)
          self.pepa_x = 0
          self.pepa_y = 0
          self.senal_mostrar_pepa.emit(self.pepa.x, self.pepa.y)
     
     @classmethod
     def from_file(cls, filepath):
          with open(filepath, 'r') as file:
               columnas = file.readline().strip().split(';')
               filas = file.readline().strip().split(';')

          columnas = [list(map(int, col.split(','))) if col != '-' else [] for col in columnas]
          filas = [list(map(int, fila.split(','))) if fila != '-' else [] for fila in filas]

          n = max(len(filas), len(columnas))
          return cls(n, filas, columnas)
     
class Tiempo(QObject):
     senal_actualizar_tiempo = pyqtSignal(str)

     def __init__(self):
          super().__init__()
          self.tiempo_restante = p.TIEMPO_JUEGO
          self.jugando = False
          self.timer = QTimer()
          self.timer.timeout.connect(self.reducir_tiempo)

     def iniciar_juego(self):
          self.tiempo_restante = p.TIEMPO_JUEGO
          self.jugando = True
          self.timer.start(1000)

     def reducir_tiempo(self):
          if self.jugando and self.tiempo_restante > 0:
               self.tiempo_restante -= 1
               minutos = self.tiempo_restante // 60
               segundos = self.tiempo_restante % 60
               tiempo_formateado = f"{minutos:02}:{segundos:02}"
               self.senal_actualizar_tiempo.emit(tiempo_formateado)
          else:
               self.timer.stop()

     def pausar_juego(self):
          self.jugando = not self.jugando
          if self.jugando:
               self.timer.start(1000)
          else:
               self.timer.stop()

     def agregar_tiempo(self, tiempo_adicional):
          self.tiempo_restante += tiempo_adicional
