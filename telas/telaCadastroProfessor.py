# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaCadastroProfessor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you sabe o que está fazendo.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CadastroProfessorWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Label para o nome do professor
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.label_nome.setObjectName("label_nome")

        # Campo de texto para o nome do professor
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setGeometry(QtCore.QRect(10, 50, 380, 30))
        self.lineEdit_nome.setObjectName("lineEdit_nome")

        # Label para o email do professor
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(10, 90, 121, 16))
        self.label_email.setObjectName("label_email")

        # Campo de texto para o email do professor
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(10, 110, 380, 30))
        self.lineEdit_email.setObjectName("lineEdit_email")

        # Label para o telefone do professor
        self.label_telefone = QtWidgets.QLabel(self.centralwidget)
        self.label_telefone.setGeometry(QtCore.QRect(10, 150, 121, 16))
        self.label_telefone.setObjectName("label_telefone")

        # Campo de texto para o telefone do professor
        self.lineEdit_telefone = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_telefone.setGeometry(QtCore.QRect(10, 170, 380, 30))
        self.lineEdit_telefone.setObjectName("lineEdit_telefone")

        # Label para a especialidade do professor
        self.label_especialidade = QtWidgets.QLabel(self.centralwidget)
        self.label_especialidade.setGeometry(QtCore.QRect(10, 210, 121, 16))
        self.label_especialidade.setObjectName("label_especialidade")

        # Campo de texto para a especialidade do professor
        self.lineEdit_especialidade = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_especialidade.setGeometry(QtCore.QRect(10, 230, 380, 30))
        self.lineEdit_especialidade.setObjectName("lineEdit_especialidade")

        # Botão de salvar
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setGeometry(QtCore.QRect(10, 270, 80, 30))
        self.pushButton_salvar.setObjectName("pushButton_salvar")

        # Botão de cancelar
        self.pushButton_cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancelar.setGeometry(QtCore.QRect(100, 270, 80, 30))
        self.pushButton_cancelar.setObjectName("pushButton_cancelar")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro de Professor"))
        self.label_nome.setText(_translate("MainWindow", "Nome:"))
        self.label_email.setText(_translate("MainWindow", "Email:"))
        self.label_telefone.setText(_translate("MainWindow", "Telefone:"))
        self.label_especialidade.setText(_translate("MainWindow", "Especialidade:"))
        self.pushButton_salvar.setText(_translate("MainWindow", "Salvar"))
        self.pushButton_cancelar.setText(_translate("MainWindow", "Cancelar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_CadastroProfessorWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
