from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QGroupBox, QGridLayout
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt


class ventanaTuplas(QWidget):
    def __init__(self):
        super().__init__()

        # Set up window properties
        self.title = 'Mi aplicación'
        self.left = 80
        self.top = 80
        self.width = 300
        self.height = 320

        self.inicializar_GUI()

    def inicializar_GUI(self):
        # inicializamos la ventana
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)



        self.show()
