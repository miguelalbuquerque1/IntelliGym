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
from telas.telaCadastroAluno import Ui_CadastroAlunoDialog
from telas.telaCadastroProfessor import Ui_CadastroProfessorWindow
from telas.telaCadastroTurma import Ui_CadastroTurmaWindow

class GerenciadorJanela:
    def __init__(self):
        self.janela_atual = None

    def trocar_janela(self, nova_janela):
        if self.janela_atual is not None:
            self.janela_atual.close()
        self.janela_atual = nova_janela
        self.janela_atual.show()

# Inicialização do Gerenciador
gerenciador = GerenciadorJanela()


class telaPrincipalAcademia(QMainWindow):
    def __init__(self, email, *args, **argvs):
        super(telaPrincipalAcademia, self).__init__(*args, **argvs)
        self.ui = Ui_AcademiaMainWindow()
        self.ui.setupUi(self)

        # Obter o ID do usuário logado pelo e-mail
        self.admin_id = self.buscar_id_por_email(email)
        if not self.admin_id:
            QMessageBox.critical(self, "Erro", "Não foi possível identificar o usuário logado!")
            sys.exit()

        # Conectar o item 'Listar' no menu para a função de listar academias
        self.ui.actionListar.triggered.connect(self.listar_academias)
        self.ui.actionListar_3.triggered.connect(self.goToProfessor) #Trigger para a janela de Professor
        self.ui.actionListar_4.triggered.connect(self.goToTurma) #Trigger para a janela de Turmas   
        self.ui.actionListar_5.triggered.connect(self.goToAluno) #Trigger para a janela de Alunos
        self.ui.actionVoltar_ao_Login.triggered.connect(self.goToLogin) #Trigger para a janela de volta ao login
        self.ui.pushButton_2.clicked.connect(self.abrir_janela_cadastro_academia)
        self.ui.pushButton_3.clicked.connect(self.excluir_academia)

        # Adicionar evento para selecionar a linha na tabela
        self.ui.tableWidget.cellClicked.connect(self.selecionar_academia)

        self.academia_selecionada_id = None  # Variável para armazenar o ID da academia selecionada

    def goToLogin(self):
        nova_janela = telaLogin()
        gerenciador.trocar_janela(self,nova_janela)
    
    def goToProfessor(self):
        self.window = telaPrincipalProfessor()
        self.window.show()
        self.close()
    
    def goToAluno(self):
        self.window = telaPrincipalAluno()
        self.window.show()
        self.close()
    
    def goToTurma(self):
        self.window = telaPrincipalTurma()
        self.window.show()
        self.close()

    @staticmethod
    def buscar_id_por_email(email):
        try:
            conn = sqlite3.connect('academia.db')
            cursor = conn.cursor()

            # Consulta para buscar o ID com base no e-mail
            cursor.execute("SELECT id FROM Usuarios WHERE email = ?", (email,))
            resultado = cursor.fetchone()

            conn.close()

            # Retorna o ID se encontrado, caso contrário retorna None
            if resultado:
                return resultado[0]
            return None
        except sqlite3.Error as e:
            print(f"Erro ao buscar ID por e-mail: {e}")
            return None

    def abrir_janela_cadastro_academia(self):
        # Passar o admin_id para a tela de cadastro de academia
        self.window = telaCadastroAcademia(self.admin_id)
        self.window.exec()

    def listar_academias(self):
        try:
            # Conexão com o banco de dados
            conn = sqlite3.connect('academia.db')
            cursor = conn.cursor()

            # Consulta SQL para buscar todas as academias
            cursor.execute("SELECT id, nome, endereco, telefone FROM Academias")
            academias = cursor.fetchall()

            # Configurar o número de linhas da tabela com base no número de academias
            self.ui.tableWidget.setRowCount(len(academias))

            # Preencher a tabela com os dados das academias
            for row_idx, academia in enumerate(academias):
                # Atribuir os dados corretamente para cada coluna
                self.ui.tableWidget.setItem(row_idx, 0, QTableWidgetItem(str(academia[0])))  # ID
                self.ui.tableWidget.setItem(row_idx, 1, QTableWidgetItem(academia[1]))  # Nome
                self.ui.tableWidget.setItem(row_idx, 2, QTableWidgetItem(academia[3]))  # Telefone
                self.ui.tableWidget.setItem(row_idx, 3, QTableWidgetItem(academia[2]))  # Endereço

            # Fecha a conexão com o banco de dados
            conn.close()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao listar academias: {str(e)}")

    def selecionar_academia(self, row, column):
        """
        Função para capturar o ID da academia selecionada ao clicar na tabela.
        """
        academia_id_item = self.ui.tableWidget.item(row, 0)  # A primeira coluna é o ID
        if academia_id_item:
            self.academia_selecionada_id = int(academia_id_item.text())  # Armazena o ID da academia
            print(f"Academia selecionada com ID: {self.academia_selecionada_id}")

    def excluir_academia(self):
        """
        Função para excluir a academia selecionada.
        """
        if self.academia_selecionada_id is None:
            QMessageBox.warning(self, "Aviso", "Selecione uma academia para excluir.")
            return

        resposta = QMessageBox.question(self, "Confirmar Exclusão", "Tem certeza que deseja excluir esta academia?",
                                        QMessageBox.Yes | QMessageBox.No)
        if resposta == QMessageBox.Yes:
            try:
                # Conexão com o banco de dados
                conn = sqlite3.connect('academia.db')
                cursor = conn.cursor()

                # Excluir a academia
                cursor.execute("DELETE FROM Academias WHERE id = ?", (self.academia_selecionada_id,))
                conn.commit()

                # Fechar a conexão
                conn.close()

                # Atualizar a lista de academias
                self.listar_academias()

                QMessageBox.information(self, "Sucesso", "Academia excluída com sucesso!")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Erro", f"Erro ao excluir academia: {str(e)}")


class telaCadastroAcademia(QDialog):
    def __init__(self, admin_id, *args, **kwargs):
        super(telaCadastroAcademia, self).__init__(*args, **kwargs)
        self.ui = Ui_CadastroAcademiaDialog()  # Supondo que você tenha a tela de cadastro de academia
        self.ui.setupUi(self)
        self.admin_id = admin_id  # Armazena o ID do usuário logado
        print(admin_id)
        # Conectar os botões
        self.ui.pushButton_salvar.clicked.connect(self.salvar_ou_atualizar_academia)
        self.ui.pushButton_cancelar.clicked.connect(self.close)

    def salvar_ou_atualizar_academia(self):
        nome = self.ui.lineEdit_nome.text()
        endereco = self.ui.lineEdit_endereco.text()
        telefone = self.ui.lineEdit_telefone.text()

        if not nome or not endereco:
            QMessageBox.warning(self, "Erro", "Nome e endereço são obrigatórios!")
            return

        try:
            print("Conectando ao banco de dados...")  # Log antes de tentar a conexão
            conn = sqlite3.connect('academia.db')
            cursor = conn.cursor()

            print(f"Conectado ao banco. Tentando salvar academia: Nome={nome}, Endereço={endereco}, Telefone={telefone}, AdminID={self.admin_id}")

            # Verifica se a academia já existe (por nome e admin_id)
            cursor.execute("SELECT id FROM Academias WHERE nome = ? AND admin_id = ?", (nome, self.admin_id))
            academia_existente = cursor.fetchone()

            if academia_existente:  # Atualizar academia existente
                id_academia = academia_existente[0]
                cursor.execute("""
                    UPDATE Academias
                    SET nome = ?, endereco = ?, telefone = ?
                    WHERE id = ? AND admin_id = ?
                """, (nome, endereco, telefone, id_academia, self.admin_id))
                QMessageBox.information(self, "Sucesso", "Academia atualizada com sucesso!")
            else:  # Inserir nova academia
                cursor.execute("""
                    INSERT INTO Academias (nome, endereco, telefone, admin_id)
                    VALUES (?, ?, ?, ?)
                """, (nome, endereco, telefone, self.admin_id))
                QMessageBox.information(self, "Sucesso", "Academia cadastrada com sucesso!")

            conn.commit()
            conn.close()
            print("Academia salva ou atualizada com sucesso!")  # Log após o commit
            self.close()  # Fecha a janela após salvar ou atualizar
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar ou atualizar academia: {str(e)}")
            print(f"Erro do SQLite: {e}")  # Exibe no console para análise
        except Exception as ex:
            QMessageBox.critical(self, "Erro inesperado", f"Erro: {str(ex)}")
            print(f"Erro inesperado: {ex}")  # Exibe no console para análise

class telaPrincipalAluno(QMainWindow):
    def __init__(self, email, *args, **argvs):
        super(telaPrincipalAluno, self).__init__(*args, **argvs)
        self.ui = Ui_AlunoMainWindow()
                

class telaCadastroAluno(QDialog):
    def __init__(self, *args, **argvs):
        super(telaCadastroAluno, self).__init__(*args, **argvs)
        self.ui = Ui_CadastroAlunoDialog()  # Supondo que você tenha a tela de cadastro de academia
        self.ui.setupUi(self)

class telaPrincipalProfessor(QMainWindow):
    def __init__(self, *args, **argvs):
        super(telaPrincipalProfessor).__init__(*args, **argvs)
        self.ui = Ui_ProfessorMainWindow()
        self.ui.setupUi(self)

class telaCadastroProfessor(QDialog):
    def __init__(self, *args, **argvs):
        super(telaCadastroProfessor, self).__init__(*args, **argvs)
        self.ui = Ui_CadastroProfessorWindow()  # Supondo que você tenha a tela de cadastro de academia
        self.ui.setupUi(self)

class telaPrincipalTurma(QMainWindow):
    def __init__(self, *args, **argvs):
        super(telaPrincipalTurma).__init__(*args, **argvs)
        self.ui = Ui_TurmaMainWindow()
        self.ui.setupUi(self)

class telaCadastroTurma(QDialog):
    def __init__(self, *args, **argvs):
        super(telaCadastroTurma, self).__init__(*args, **argvs)
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
                    self.window = telaPrincipalAcademia(email)
                elif tipo_usuario == 0:  # Gerente
                    self.window = telaPrincipalAcademia(email)
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