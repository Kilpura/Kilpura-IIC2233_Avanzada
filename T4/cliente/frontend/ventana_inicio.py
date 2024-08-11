import os
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton,
                             QLineEdit, QComboBox, QScrollArea, QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt6.QtGui import QPixmap

class VentanaInicio(QWidget):
     senal_verificar_usuario = pyqtSignal(str)
     senal_salir = pyqtSignal(str)
     senal_comenzar = pyqtSignal(str)

     def __init__(self) -> None:
          super().__init__()
          self.inicializa_gui()

     def inicializa_gui(self) -> None:

          self.setStyleSheet("""
               background-color: #D4E6F1;
               color: black;
               font-size: 13pt;
          """)
          #Imagen
          self.label_imagen = QLabel(self)
          ruta_imagen = os.path.join('cliente', 'assets', 'sprites', 'logo.png')
          pixeles = QPixmap(ruta_imagen)
          self.label_imagen.setPixmap(pixeles)
          self.label_imagen.setScaledContents(True)
          self.label_imagen.setFixedSize(450, 450)

          # texto que pide elnombre de usuario
          self.label_texto_usuario = QLabel('Nombre de usuario', self)
          self.input_texto_usuario = QLineEdit(self)

          # menu de selector de puzzle
          self.label_selector_puzzle = QLabel('Selecciona el puzzle', self)
          self.combo_selector_puzzle = QComboBox(self)

          self.cargar_puzzles()

          # sección "Salon de la Fama"
          self.label_fama = QLabel('Salón de la Fama', self)
          self.scroll_fama = QScrollArea(self)
          self.scroll_fama.setWidgetResizable(True)
          self.widget_fama = QWidget()  # Crear un nuevo QWidget
          self.layout_fama = QVBoxLayout(self.widget_fama)  # Asignar un layout al QWidget
          self.cargar_fama()  # Cargar los puntajes en el layout
          self.scroll_fama.setWidget(self.widget_fama)

          # botones
          self.boton_comenzar = QPushButton('Comenzar Partida', self)
          self.boton_comenzar.clicked.connect(self.comenzar_partida)

          self.boton_salir = QPushButton('Salir', self)
          self.boton_salir.clicked.connect(self.salir_programa)

          # Layout superior
          layout_superior = QHBoxLayout()
          layout_superior.addStretch(1)
          layout_superior.addWidget(self.label_imagen)
          layout_superior.addStretch(1)

          # Layour central fama
          layout_fama = QVBoxLayout()
          layout_fama.addStretch(1)
          layout_fama.addWidget(self.label_fama)
          layout_fama.addWidget(self.scroll_fama)
          layout_fama.addStretch(1)

          # Layour central nombre de usuario
          layout_nombre = QVBoxLayout()
          layout_nombre.addStretch(1)
          layout_nombre.addWidget(self.label_texto_usuario)
          layout_nombre.addWidget(self.input_texto_usuario)
          layout_nombre.addStretch(1)

          # Layour central selector
          layout_selector = QVBoxLayout()
          layout_selector.addStretch(1)
          layout_selector.addWidget(self.label_selector_puzzle)
          layout_selector.addWidget(self.combo_selector_puzzle)
          layout_selector.addStretch(1)

          #layoutcentral
          layout_central = QHBoxLayout()
          layout_central.addStretch(1)
          layout_central.addLayout(layout_fama)
          layout_central.addStretch(1)
          layout_central.addLayout(layout_nombre)
          layout_central.addStretch(1)
          layout_central.addLayout(layout_selector)
          layout_central.addStretch(1)

          #Layout inferior
          layout_inferior = QHBoxLayout()
          layout_inferior.addWidget(self.boton_comenzar)
          layout_inferior.addWidget(self.boton_salir)
          
          # Configuración del layout
          layout = QVBoxLayout()
          layout.addLayout(layout_superior)
          layout.addLayout(layout_central)
          layout.addLayout(layout_inferior)

          self.setLayout(layout)
          self.setWindowTitle('DCCome Lechuga - Ventana de Inicio')
          self.setGeometry(450, 150, 650, 550)

          self.show()
     
     def cargar_puzzles(self):
          path = "cliente/assets/base_puzzles"

          if os.path.exists(path):
               for file_name in os.listdir(path):
                    if file_name.endswith('.txt'):
                         self.combo_selector_puzzle.addItem(file_name)

     def cargar_fama(self):
          try:
               with open('puntaje.txt', 'r') as file:
                    puntaje = file.readlines()
               puntajes = [line.strip() for line in puntajes]
               # se ordenan de manera descendente
               puntajes.sort(key=lambda x: int(x.split('-')[1]), reverse=True)

               for puntaje in puntajes:
                    label_puntaje = QLabel(puntaje, self)
                    self.layout_fama.addWidget(label_puntaje)
          
          except FileNotFoundError:
               label_no_puntajes = QLabel('Aún no hay puntajes guardados')
               self.layout_fama.addWidget(label_no_puntajes)

     def comenzar_partida(self):
          nombre_usuario = self.input_texto_usuario.text()
          self.senal_verificar_usuario.emit(nombre_usuario)

     def validacion_usuario_resultado(self, valido, mensaje):
          if valido:
               puzzle_seleccionado = self.combo_selector_puzzle.currentText()
               self.senal_comenzar.emit(puzzle_seleccionado)
          else:
               QMessageBox.critical(self, 'Error', mensaje)

     def salir_programa(self):
          self.close()