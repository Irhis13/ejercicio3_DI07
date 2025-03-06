import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

directorio_principal = os.path.dirname(__file__)


class MainWindow(QMainWindow):
   """
   Clase MainWindow que hereda de QMainWindow.

   Ventana principal de la aplicación.
   """
   def __init__(self):
       super(MainWindow, self).__init__()

       self.setWindowTitle("PySide6 executable")

       layout = QVBoxLayout()

       label = QLabel("Hola mundo!")
       label.setAlignment(Qt.AlignCenter)
       layout.addWidget(label)

       button = QPushButton("Cerrar")
       button.pressed.connect(self.close)
       layout.addWidget(button)

       widget = QWidget()
       widget.setLayout(layout)
       self.setCentralWidget(widget)

def main():
   """"
   Punto de entrada a la aplicación.

   Construye un objecto MainWindow y lo muestra.   
   """
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
  
   app.exec()




