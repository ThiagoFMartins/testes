import sqlite3

class Usuario():
    def __init__(self, login, senha, nome, proficao, genero):
        self.login = login
        self.senha = senha
        self.nome = nome
        self.proficao = proficao
        self.genero = genero

conn = sqlite3.connect('ifight.db')
cursor = conn.cursor()

cursor.execute ("""
    create table usuario 
    (
        id integer not null primary key autoincrement,
        login varchar(100),
        senha varchar (50),
        nome varchar(150) not null,
        profissao varchar (50),
        genero varchar(15)
        )
    """)

conn.close()

def exibirMenu():
    print("""
            Menu\n
            1 - Criar Usuário\n
            0 - Sair\n""")

def adicionarUsuario():

    conn = sqlite3.connect('ifight.db')
    cursor = conn.cursor()

    u_login = input("login:")
    assert "@" in u_login
    u_senha = input("senha:")
    u_nome = input("nome:")
    u_profissao = input("profissao:")
    u_genero = input("Gênero:")

    cursor.execute \
    ("""
     INSERT INTO usuario (login, senha, nome, profissao,genero)
     VALUES (?, ?, ?, ?, ?)
    """, (u_login, u_senha, u_nome, u_profissao, u_genero))

    conn.commit()

    print("ok")

    conn.close()

def main(args=[]):
    continuar = True

    while (continuar):

        exibirMenu()

        try:

            op_escolhida = int(input("Escolha uma das opções: "))
            if op_escolhida == 0:
                print("Saindo...")
                continuar = False
            elif op_escolhida == 1:
                adicionarUsuario()
            else:
                print("Opção inválida")

        except ValueError:
            print("Erro")


if (__name__ == "__main__"):
    main()