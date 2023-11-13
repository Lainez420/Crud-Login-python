# @autor: Alejandro Lainez Gonzalez
# @fecha: 2023/10/24
# @ficha: 2740559
#descripciom: modulo para la ventana de dialogo para buscaminas.ui


# Modulos o paquetes de pyqt5
# Tener en cuenta la instalacion de (pyqt5) si no 
# lo tenemos  lo instalamos asi. pip pyqtr5
# En el cdm
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class DlgBuscaminas(QDialog):
    def __init__(self):
        super(DlgBuscaminas, self). __init__()
        loadUi('app_escritorio/buscaminas.ui', self)

        self.bttnCelda1.clicked.connect(self.celda11)
    

    def celda11(self):
        self.bttnCelda1.setText("1,1")
        self.bttnCelda1.isEnabled = True

