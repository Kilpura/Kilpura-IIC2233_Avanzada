from backend.controlador import Controlador
import sys
from PyQt6.QtWidgets import (QApplication)

def main():
    app = QApplication(sys.argv)
    controlador = Controlador()
    controlador.iniciar()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()