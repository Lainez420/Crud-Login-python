# @autor: Alejandro Lainez Gonzalez
# @fecha: 2023/10/24
# @ficha: 2740559
# descripciom: programa principal para el aplicativo


# Modulos o paquetes de pyqt5
# Tener en cuenta la instalacion de (pyqt5) si no
# lo tenemos  lo instalamos asi. pip pyqtr5
# En el cdm
import time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from modulobm.dialogo_principal import DlgPrincipal as dlgbm
import sys
from mysql import connector


## classe para implementar la funcionalidad de la ventana de dialogo
## para el inicio de sesion
class DlgInicio(QDialog):
    def __init__(self):
        super(DlgInicio, self).__init__()
        loadUi("app_escritorio/inicio_sesion.ui", self)

        self.bttnInicio.clicked.connect(self.inicio)
        self.btncerrar1.clicked.connect(self.cerra1)

    ## funcion que se ejecuta al precionar el boton inicio
    def inicio(self):
        print("se ha presionado el boton 'bttnInicio'")

        usuario = self.txtUsuario.text()
        clave = self.txtClave.text()
        misitioalg = connector.connect(
            host="localhost", user="root", password="", database="misitioalg"
        )
        micursor = misitioalg.cursor()

        micursor.execute(
            "SELECT usuario, clave FROM usuarios WHERE usuario = '"
            + usuario
            + "' AND clave = '"
            + clave
            + "'"
        )
        registro = micursor.fetchall()

        if registro:
            usu = registro[0][0]
            self.busca = dlgbm(usu)
            self.busca.show()
            # self.close()
        else:
            # time.sleep(2)5
            self.Lbcontrasea.setText(" Usuario y contraseña incorrectas ...")

    def cerra1(self):
        self.close()


# programa principal
app = QApplication(sys.argv)
DlgInicio = DlgInicio()  # objDialogo: objeto
DlgInicio.show()
sys.exit(app.exec_())
