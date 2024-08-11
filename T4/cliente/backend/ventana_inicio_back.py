from PyQt6.QtCore import QObject, pyqtSignal

class Procesador(QObject):
     senal_validacion_usuario = pyqtSignal(bool, str)
     senal_comienza = pyqtSignal(str)

     def __init__(self):
          super().__init__()

     def validar_usuario(self, nombre_usuario):
          if not nombre_usuario:
               self.senal_validacion_usuario.emit(False, "El nombre no puede estar vacío.")
               return
          if not any(char.isupper() for char in nombre_usuario):
               self.senal_validacion_usuario.emit(False, "El nombre debe contener al menos una mayúscula.")
               return
          if not any(char.isdigit() for char in nombre_usuario):
               self.senal_validacion_usuario.emit(False, "El nombre debe contener al menos un número.")
               return
          if not nombre_usuario.isalnum():
               self.senal_validacion_usuario.emit(False, "El nombre debe ser alfanumérico.")
               return
          self.senal_validacion_usuario.emit(True, "")
     
     def comenzar(self, puzzle):
          self.senal_comienza.emit(f"Buena suerte! tu puzzle es {puzzle}!")
          return