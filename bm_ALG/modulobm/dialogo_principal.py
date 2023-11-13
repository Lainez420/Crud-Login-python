# @ Autor : Alejandro Lainez Gonzalez
# @ Fecha : 31 / 10 / 2023
# @ Descripción: Modulo para la ventana de dialogo buscaminas.ui

# Módulos o paquetes propios de python

# Modulos de MySQL
import mysql
from mysql import connector
from PyQt5 import QtWidgets
import time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi



import sys
from mysql import connector


class DlgPrincipal(QDialog):
    def __init__(self, usu):
        super(DlgPrincipal, self).__init__()
        loadUi("app_escritorio/inicio_sesion_2.ui", self)
        self.usu = usu
        
        self.lbmensajeee.setText(usu)
        self.setFixedWidth(650)
        self.setFixedHeight(400)
        self.btnInsertar.clicked.connect(self.insertar)
        self.tblWdgtUsuarios.clicked.connect(self.men)
        self.bttCerrar2.clicked.connect(self.cerra2)
        self.btnActualizar.clicked.connect(self.actualizar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.tblWdgtUsuarios.clicked.connect(self.filaElegida)
       

        nombreColumnas = [
            {"nombre_col": "id", "longitud": 100},
            {"nombre_col": "usuario", "longitud": 120},
            {"nombre_col": "clave", "longitud": 120},
            {"nombre_col": "correo", "longitud": 190},
        ]
        # ajustar el nombre de las columnas  de la tabla
        self.tblWdgtUsuarios.setColumnCount(len(nombreColumnas))
        # establecer el tamaño de cada columna de la tabla
        nombre_col = []
        for i in range(len(nombreColumnas)):
            self.tblWdgtUsuarios.setColumnWidth(i, nombreColumnas[i]["longitud"])
            nombre_col.append(nombreColumnas[i]["nombre_col"])

        self.tblWdgtUsuarios.setHorizontalHeaderLabels(nombre_col)
        self.cargar_datos()



    def filaElegida(self):
        fila = self.tblWdgtUsuarios.currentRow()
        id_usuario = self.tblWdgtUsuarios.item(fila, 0)
        usuarios = self.tblWdgtUsuarios.item(fila,1)
        clave = self.tblWdgtUsuarios.item(fila,2)
        correo = self.tblWdgtUsuarios.item(fila,3)

        self.spincontro.setValue(int(id_usuario.text()))
        self.txtUsuarioo.setText(usuarios.text())
        self.txtClavee.setText(clave.text())
        self.txtCorreo.setText(correo.text())

    def cargar_datos(self):
        misitioalg = connector.connect(
            host="localhost", user="root", password="", database="misitioalg"
        )
        miCursor = misitioalg.cursor()
        stmt = "SELECT id, usuario, clave,correo FROM usuarios"
        miCursor.execute(stmt)

        registros = miCursor.fetchall()
        nroRegistro = len(registros)
        self.tblWdgtUsuarios.setRowCount(nroRegistro)
        fila = 0

        for registro in registros:
            self.tblWdgtUsuarios.setItem(
                fila, 0, QtWidgets.QTableWidgetItem(str(registro[0]))
            )
            self.tblWdgtUsuarios.setItem(
                fila, 1, QtWidgets.QTableWidgetItem(registro[1])
            )
            self.tblWdgtUsuarios.setItem(
                fila, 2, QtWidgets.QTableWidgetItem(registro[2])
            )
            self.tblWdgtUsuarios.setItem(
                fila, 3, QtWidgets.QTableWidgetItem(registro[3])
            )
            fila += 1

    # funcion para cerrar la segunda ventana despues del login
    def cerra2(self):
        self.close()

    # funcion para  insertar un elemento en la base de datos
    def insertar(self):
        misitioalg = connector.connect(
            host="localhost", user="root", password="", database="misitioalg"
        )
        micursor = misitioalg.cursor()

        stmt = "INSERT INTO usuarios (usuario, clave, correo) VALUES (%s, %s, %s)"

        usuario = self.txtUsuarioo.text()
        clave = self.txtClavee.text()
        correo = self.txtCorreo.text()
        valores = (usuario, clave, correo)
        misitioalg.commit()
        micursor.execute(stmt, valores)

        # micursor.commit()
        self.cargar_datos()
        

        self.txtUsuarioo.setText("")
        self.txtClavee.setText("")
        self.txtCorreo.setText("")

    # funcion para eliminar un elemento de la base de datos
    def eliminar(self):
        misitioalg = connector.connect(
            host="localhost", user="root", password="", database="misitioalg"
        )
        micursor = misitioalg.cursor()

        fila = self.tblWdgtUsuarios.currentRow()
        id_usuario = self.tblWdgtUsuarios.item(fila, 0)
        # print("el numero es ", self.spincontro.value(), ",", fila, id_usuario.text())
        self.spincontro.setValue(int(id_usuario.text()))
        if id_usuario is not None:
            valor1 = id_usuario.text()
            sql = "DELETE FROM usuarios WHERE id = %s"
            micursor.execute(sql, (valor1,))
            misitioalg.commit()

    def actualizar(self):
        misitioalg = connector.connect(
            host="localhost", user="root", password="", database="misitioalg"
        )
        micursor = misitioalg.cursor()

        fila = self.tblWdgtUsuarios.currentRow()
        id_usuario = self.tblWdgtUsuarios.item(fila, 0)
        # print("el numero es ", self.spincontro.value(), ",", fila, id_usuario.text())
        self.spincontro.setValue(int(id_usuario.text()))

        if id_usuario is not None:
            consulta = "UPDATE usuarios SET usuario = %s, clave = %s, correo = %s WHERE id = %s"

            usuario = self.txtUsuarioo.text()
            clave = self.txtClavee.text()
            correo = self.txtCorreo.text()
            id_usuarioo = id_usuario.text()
            valores = (usuario, clave, correo, id_usuarioo)
            micursor.execute(consulta, (valores))

            self.cargar_datos()
            misitioalg.commit()
            self.txtUsuarioo.setText("")
            self.txtClavee.setText("")
            self.txtCorreo.setText("")

    def men(self):
        fila = self.tblWdgtUsuarios.currentRow()
        id_usuario = self.tblWdgtUsuarios.item(fila, 0)
        # print("el numero es ", self.spincontro.value(), ",", fila, id_usuario.text())
        self.spincontro.setValue(int(id_usuario.text()))

  



    # def actualizar(self):
    #     misitioalg = connector.connect(
    #         host="localhost", user="root", password="", database="misitioalg"
    #     )
    #     micursor = misitioalg.cursor()

    #     fila = self.tblWdgtUsuarios.currentRow()
    #     id_usuario = self.tblWdgtUsuarios.item(fila, 0)
    #     # print("el numero es ", self.spincontro.value(), ",", fila, id_usuario.text())
    #     self.spincontro.setValue(int(id_usuario.text()))

    #     consulta = "UPDATE usuarioss SET usuario = %s, clave = %s, correo = %s WHERE id_usuario = %s"

    #     usuario = self.txtUsuarioo.text()
    #     clave = self.txtClavee.text()
    #     correo = self.txtCorreo.text()
    #     id = id_usuario.text()
    #     valores = (usuario, clave, correo, id)
    #     micursor.execute(consulta, valores)

    #     # micursor.commit()
    #     self.cargar_datos()
    #     misitioalg.commit()

    #     self.txtUsuarioo.setText("")
    #     self.txtClavee.setText("")
    #     self.txtCorreo.setText("")
