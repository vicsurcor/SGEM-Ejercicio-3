import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QHBoxLayout

#el controlador debe conocer el modelo
import Vistas.V1

class ControladorHolaMundo():
    # Método constructor de la clase
    def __init__(self,Ventana):
        self.saludo=Saludo
        self.ventana=Ventana
    def handler_saludar(self):
        if self.saludo.saludar=="Hola mundo" :
            # Actualizar modelo Saludo
            self.saludo.saludar = "Adiossss"

        else:
            # Actualizar modelo
            self.saludo.saludar = "Hola mundo"

        # Actualizar ventana
        self.ventana.label.setText(self.saludo.saludar)
