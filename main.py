from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
from PyQt5.uic import loadUi
import os, sys

import sqlite3
from db.query import sqlite_db
from db.query import adicionar_usuario
from db.query import verificar_usuario
from telas.telaLogin import Ui_LoginDialog
from telas.telaCadastroUsuario import Ui_CadastroUsuarioDialog
from telas.telaPrincipalAluno import Ui_AlunoMainWindow
from telas.telaPrincipalAcademia import Ui_AcademiaMainWindow
from telas.telaPrincipalProfessor import Ui_ProfessorMainWindow
from telas.telaPrincipalTurma import Ui_TurmaMainWindow
from telas.telaCadastroAcademia import Ui_CadastroAcademiaDialog
from telas.telaCadastroAluno import Ui_CadastroAlunoWindow
from telas.telaCadastroProfessor import Ui_CadastroProfessorWindow
from telas.telaCadastroTurma import Ui_CadastroTurmaWindow


class telaPrincipalAcademia(QMainWindow):
    def __init__(self, *args, **argvs):
        super(telaPrincipalAcademia, self).__init__(*args, **argvs)
        self.ui = Ui_AcademiaMainWindow()
        self.ui.setupUi(self)

        # Conectar o item 'Listar' no menu para a função de listar academias
        self.ui.actionListar.triggered.connect(self.listar_academias)
        self.ui.actionCadastrar.triggered.connect(self.abrir_janela_cadastro_academia)

    def abrir_janela_cadastro_academia(self):
        self.window = telaCadastroAcademia()
        self.window.exec()

    def listar_academias(self):
        try:
            # Conexão com o banco de dados
            conn = sqlite3.connect('academia.db')
            cursor = conn.cursor()

            # Consulta SQL para buscar todas as academias
            cursor.execute("SELECT id, nome, endereco, telefone FROM Academias")  # Modifique conforme o seu modelo de banco
            academias = cursor.fetchall()

            # Configurar o número de linhas da tabela com base no número de academias
            self.ui.tableWidget.setRowCount(len(academias))

            # Preencher a tabela com os dados das academias
            for row_idx, academia in enumerate(academias):
                for col_idx, data in enumerate(academia):
                    self.ui.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

            # Fecha a conexão com o banco de dados
            conn.close()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao listar academias: {str(e)}")

class telaCadastroAcademia(QDialog):
    def __init__(self, *args, **kwargs):
        super(telaCadastroAcademia, self).__init__(*args, **kwargs)
        self.ui = Ui_CadastroAcademiaDialog()  # Supondo que você tenha a tela de cadastro de academia
        self.ui.setupUi(self)

        # Conectar o botão de salvar para chamar o método de salvar ou atualizar academia
        self.ui.pushButton_salvar.clicked.connect(self.salvar_ou_atualizar_academia)
        self.ui.pushButton_cancelar.clicked.connect(self.close)

    def salvar_ou_atualizar_academia(self):
        nome = self.ui.lineEditNome.text()
        endereco = self.ui.lineEditEndereco.text()
        telefone = self.ui.lineEditTelefone.text()

        if not nome or not endereco:
            QMessageBox.warning(self, "Erro", "Nome e endereço são obrigatórios!")
            return

        try:
            # Verifica se a academia já existe (por nome ou id)
            conn = sqlite3.connect('academia.db')
            cursor = conn.cursor()

            # Debugging
            print(f"Tentando salvar academia: Nome={nome}, Endereço={endereco}, Telefone={telefone}")

            cursor.execute("SELECT id FROM Academias WHERE nome = ?", (nome,))
            academia_existente = cursor.fetchone()

            if academia_existente:  # Se a academia existe, atualize
                id_academia = academia_existente[0]
                cursor.execute("""
                    UPDATE Academias
                    SET nome = ?, endereco = ?, telefone = ?
                    WHERE id = ?
                """, (nome, endereco, telefone, id_academia))
                QMessageBox.information(self, "Sucesso", "Academia atualizada com sucesso!")
            else:  # Caso contrário, insira uma nova academia
                cursor.execute("""
                    INSERT INTO Academias (nome, endereco, telefone)
                    VALUES (?, ?, ?)
                """, (nome, endereco, telefone))
                QMessageBox.information(self, "Sucesso", "Academia cadastrada com sucesso!")

            conn.commit()
            conn.close()
            self.close()  # Fecha a janela após salvar ou atualizar
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar ou atualizar academia: {str(e)}")
            print(f"Erro do SQLite: {e}")  # Exibe no console para análise
        except Exception as ex:
            QMessageBox.critical(self, "Erro inesperado", f"Erro: {str(ex)}")
            print(f"Erro inesperado: {ex}")  # Exibe no console para análise


class telaPrincipalAluno(QMainWindow):
    def __init__(self, *args, **argvs):
        super(telaPrincipalAluno).__init__(*args, **argvs)
        self.ui = Ui_AlunoMainWindow()
        self.ui.setupUi(self)

class telaCadastroAluno(QDialog):
    def __init__(self, *args, **kwargs):
        super(telaCadastroAluno, self).__init__(*args, **kwargs)
        self.ui = Ui_CadastroAlunoWindow()  # Supondo que você tenha a tela de cadastro de academia
        self.ui.setupUi(self)

class telaPrincipalProfessor(QMainWindow):
    def __init__(self, *args, **argvs):
        super(telaPrincipalProfessor).__init__(*args, **argvs)
        self.ui = Ui_ProfessorMainWindow()
        self.ui.setupUi(self)

class telaCadastroProfessor(QDialog):
    def __init__(self, *args, **kwargs):
        super(telaCadastroProfessor, self).__init__(*args, **kwargs)
        self.ui = Ui_CadastroProfessorWindow()  # Supondo que você tenha a tela de cadastro de academia
        self.ui.setupUi(self)

class telaPrincipalTurma(QMainWindow):
    def __init__(self, *args, **argvs):
        super(telaPrincipalTurma).__init__(*args, **argvs)
        self.ui = Ui_TurmaMainWindow()
        self.ui.setupUi(self)

class telaCadastroTurma(QDialog):
    def __init__(self, *args, **kwargs):
        super(telaCadastroTurma, self).__init__(*args, **kwargs)
        self.ui = Ui_CadastroTurmaWindow()  # Supondo que você tenha a tela de cadastro de academia
        self.ui.setupUi(self)

class telaCadastroUsuario(QDialog):
    def __init__(self, *args, **argvs):
        super(telaCadastroUsuario, self).__init__(*args, **argvs)
        self.ui = Ui_CadastroUsuarioDialog()
        self.ui.setupUi(self)
        self.ui.btnRegistra.clicked.connect(self.cadastraUsuario)
        self.ui.btnCancela.clicked.connect(self.cancelaCadastro)

    def cadastraUsuario(self):
        # Obtenha os dados dos campos de entrada
        nome_usuario = self.ui.lineEdit_nome.text()  # Campo de nome
        email_usuario = self.ui.lineEdit_email.text()  # Campo de email
        senha_usuario = self.ui.lineEdit_senha.text()  # Campo de senha
        tipo_usuario = 1 if self.ui.checkBoxAdmin.isChecked() else 0  # 1 para admin, 2 para gerente

        if not nome_usuario or not email_usuario or not senha_usuario:
            QMessageBox.warning(self, "Erro", "Todos os campos devem ser preenchidos!")
            return

        try:
            # Tente adicionar o usuário ao banco de dados
            adicionar_usuario(nome_usuario, email_usuario, senha_usuario, tipo_usuario)
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso!")
            self.cancelaCadastro()  # Voltar para a tela de login
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao cadastrar usuário: {str(e)}")

    def cancelaCadastro(self):
        self.window = telaLogin()
        self.window.show()
        self.close()


class telaLogin(QDialog):
    def __init__(self, *args, **argvs):
        super(telaLogin, self).__init__(*args, **argvs)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.ui.btnLogin.clicked.connect(self.login)
        self.ui.btnRegistrar.clicked.connect(self.goToCadastrar)

    def login(self):
        email = self.ui.lineEdit_2.text()  # Campo de email
        senha = self.ui.lineEdit.text()   # Campo de senha

        if not email or not senha:
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos!")
            return

        try:
            # Verifica se o usuário existe no banco de dados
            usuario = verificar_usuario(email, senha)
            if usuario:
                tipo_usuario = usuario[4]  # Supondo que a coluna 'tipo' esteja no índice 4
                QMessageBox.information(self, "Login realizado", f"Bem-vindo, {usuario[1]}!")  # Supondo nome no índice 1

                # Abrir a tela correspondente ao tipo de usuário
                if tipo_usuario == 1:  # Admin
                    self.window = telaPrincipalAcademia()
                elif tipo_usuario == 0:  # Gerente
                    self.window = telaPrincipalAcademia()
                else:
                    QMessageBox.warning(self, "Erro", "Tipo de usuário inválido!")
                    return

                self.window.show()
                self.close()
            else:
                QMessageBox.warning(self, "Erro", "E-mail ou senha incorretos!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao tentar realizar login: {str(e)}")

    def goToCadastrar(self):
        self.window = telaCadastroUsuario()
        self.window.show()
        self.close()


app = QApplication(sys.argv)
window = telaLogin()
window.show()
sys.exit(app.exec_())