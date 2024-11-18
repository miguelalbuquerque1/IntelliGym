import sqlite3

def sqlite_db():
    # Conectar ao banco de dados (ou criar, caso não exista)
    conn = sqlite3.connect('academia.db')
    cursor = conn.cursor()

    # Criação das tabelas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        tipo INTEGER
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Academias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        endereco TEXT,
        telefone TEXT,
        admin_id INTEGER,
        FOREIGN KEY (admin_id) REFERENCES Usuarios (id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE,
        telefone TEXT,
        data_nascimento DATE,
        academia_id INTEGER NOT NULL,
        turma_id INTEGER,
        FOREIGN KEY (academia_id) REFERENCES Academias (id),
        FOREIGN KEY (turma_id) REFERENCES Turmas (id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE,
        telefone TEXT,
        especialidade TEXT,
        academia_id INTEGER NOT NULL,
        FOREIGN KEY (academia_id) REFERENCES Academias (id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Turmas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        horario TEXT,
        modalidade TEXT,
        academia_id INTEGER NOT NULL,
        professor_id INTEGER NOT NULL,
        FOREIGN KEY (academia_id) REFERENCES Academias (id),
        FOREIGN KEY (professor_id) REFERENCES Professores (id)
    );
    """)

    # Confirmar alterações e fechar conexão
    conn.commit()
    conn.close()

    print("Banco de dados e tabelas criados com sucesso!")


def adicionar_usuario(nome, email, senha, tipo):
    conn = sqlite3.connect('academia.db')
    cursor = conn.cursor()

    # Verifica se o usuário já existe
    cursor.execute("SELECT * FROM Usuarios WHERE email = ?", (email,))
    if cursor.fetchone():
        raise Exception("E-mail já cadastrado.")

    # Insere o novo usuário
    cursor.execute("""
        INSERT INTO Usuarios (nome, email, senha, tipo)
        VALUES (?, ?, ?, ?)
    """, (nome, email, senha, tipo))
    conn.commit()
    conn.close()

def verificar_usuario(email, senha):
    conn = sqlite3.connect('academia.db')
    cursor = conn.cursor()

    # Verifica se existe um usuário com o e-mail e senha fornecidos
    cursor.execute("SELECT * FROM Usuarios WHERE email = ? AND senha = ?", (email, senha))
    usuario = cursor.fetchone()

    conn.close()
    return usuario  # Retorna o usuário encontrado ou None


# Executar a função
if __name__ == "__main__":
    sqlite_db()