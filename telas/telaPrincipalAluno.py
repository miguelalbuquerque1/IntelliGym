from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AlunoMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 488)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 511, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        
        # Configuração das colunas
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)  # ID
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)  # Nome
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)  # Idade
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)  # Peso
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)  # Telefone

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.label.setObjectName("label")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 261, 20))
        self.lineEdit.setObjectName("lineEdit")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 30, 71, 21))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 420, 81, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 420, 71, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuInicio = QtWidgets.QMenu(self.menubar)
        self.menuInicio.setObjectName("menuInicio")
        
        self.menuProfessores = QtWidgets.QMenu(self.menubar)
        self.menuProfessores.setObjectName("menuProfessores")
        
        self.menuTurmas = QtWidgets.QMenu(self.menubar)
        self.menuTurmas.setObjectName("menuTurmas")
        
        self.menuAlunos = QtWidgets.QMenu(self.menubar)
        self.menuAlunos.setObjectName("menuAlunos")
        
        self.menuSair = QtWidgets.QMenu(self.menubar)
        self.menuSair.setObjectName("menuSair")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionListar = QtWidgets.QAction(MainWindow)
        self.actionListar.setObjectName("actionListar")
        
        self.actionListar_3 = QtWidgets.QAction(MainWindow)
        self.actionListar_3.setObjectName("actionListar_3")
        
        self.actionListar_4 = QtWidgets.QAction(MainWindow)
        self.actionListar_4.setObjectName("actionListar_4")
        
        self.actionListar_5 = QtWidgets.QAction(MainWindow)
        self.actionListar_5.setObjectName("actionListar_5")
        
        self.actionVoltar_ao_Login = QtWidgets.QAction(MainWindow)
        self.actionVoltar_ao_Login.setObjectName("actionVoltar_ao_Login")
        
        self.menuInicio.addAction(self.actionListar)
        self.menuProfessores.addAction(self.actionListar_3)
        self.menuTurmas.addAction(self.actionListar_4)
        self.menuAlunos.addAction(self.actionListar_5)
        self.menuSair.addAction(self.actionVoltar_ao_Login)
        
        self.menubar.addAction(self.menuInicio.menuAction())
        self.menubar.addAction(self.menuProfessores.menuAction())
        self.menubar.addAction(self.menuTurmas.menuAction())
        self.menubar.addAction(self.menuAlunos.menuAction())
        self.menubar.addAction(self.menuSair.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aluno"))
        
        # Alterando os textos das colunas para refletir a troca
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Idade"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Peso"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Telefone"))
        
        self.label.setText(_translate("MainWindow", "Listagem de Alunos:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Pesquisar"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.pushButton_2.setText(_translate("MainWindow", "ADICIONAR"))
        self.pushButton_3.setText(_translate("MainWindow", "EXCLUIR"))
        self.menuInicio.setTitle(_translate("MainWindow", "Academias"))
        self.menuProfessores.setTitle(_translate("MainWindow", "Professores"))
        self.menuTurmas.setTitle(_translate("MainWindow", "Turmas"))
        self.menuAlunos.setTitle(_translate("MainWindow", "Alunos"))
        self.menuSair.setTitle(_translate("MainWindow", "Sair"))
        self.actionListar.setText(_translate("MainWindow", "Listar"))
        self.actionListar_3.setText(_translate("MainWindow", "Listar"))
        self.actionListar_4.setText(_translate("MainWindow", "Listar"))
        self.actionListar_5.setText(_translate("MainWindow", "Listar"))
        self.actionVoltar_ao_Login.setText(_translate("MainWindow", "Voltar ao Login"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AlunoMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
