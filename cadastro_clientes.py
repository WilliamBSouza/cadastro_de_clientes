import sqlite3
import os

def limpa_terminal():
    if os.name == 'nt':
        os.system('cls')

    else:
        os.system('clear')

conexao = sqlite3.connect('cadastro_clientes.db')
cursor = conexao.cursor()

# Cria a tabela
#cursor.execute('CREATE TABLE clientes (id INT, nome VARCHAR(45), idade INT, endereco VARCHAR(50), telefone VARCHAR(15))')

def exibir_clientes():
    
    #limpa o terminal
    limpa_terminal()
    print("*" * 50)
    # Executa a consulta SELECT em ordem crescente por id ORDER BY
    cursor.execute('SELECT * FROM clientes ORDER BY id ASC')

    # Recupera todos os registros
    registros = cursor.fetchall()

    # Exibe os registros
    for registro in registros:
        print(registro)
    
    print("*" * 50)

def add_clientes():

    #limpa o terminal
    limpa_terminal()
    print("-" * 50)
    codigo_cliente = input("Digite o código do cliente: ")
    nome_cliente = input("Digite o nome do cliente: ")
    idade_cliente = input("Digite a idade do cliente: ")
    endereco_do_cliente = input("Digite o endereço do cliente: ")
    telefone_do_cliente = input("Digite o telefone do cliente: ")

    cursor.execute('INSERT INTO clientes VALUES(?,?,?,?,?)', (codigo_cliente, nome_cliente, idade_cliente, endereco_do_cliente, telefone_do_cliente))

    # Confirma as alterações
    conexao.commit()

    print("Cliente adicionado com sucesso!")
    print("-" * 50)

def delete_cliente(id):

    #limpa o terminal
    limpa_terminal()

    print("-" * 50)
    
    conexao = sqlite3.connect('cadastro_clientes.db')
    cursor = conexao.cursor()

    # Executa a instrução DELETE
    cursor.execute('DELETE FROM clientes WHERE id = ?', (id,))

    # Confirma as alterações
    conexao.commit()

    # Fecha a conexão
    conexao.close()
    print("Cliente deletado com sucesso!")
    print("-" * 50)

def editar_cliente(id_cliente):

    print("-" * 50)

    conexao = sqlite3.connect('cadastro_clientes.db')
    cursor = conexao.cursor()

    # Solicita o campo a ser editado
    campo = input("""Digite a infotmação a ser editada:
                   [1] id
                   [2] nome
                   [3] idade
                   [4] endereco
                   [5] telefone 
                   Opção: """)
    
    if campo == "1":
        campo = "id"
    elif campo == "2":
        campo = "nome"
    elif campo == "3":
        campo = "idade"
    elif campo == "4":
        campo = "endereco"
    elif campo == "5":
        campo = "telefone"
    else:
        print("Opção inválida. Saindo...")
        return
    
    print("você está esditando", campo)

    novo_valor = input("Digite o novo valor: ")

    # Executa a instrução UPDATE
    cursor.execute(f'UPDATE clientes SET {campo} = ? WHERE id = ?', (novo_valor, id_cliente))

    # Confirma as alterações
    conexao.commit()

    # Fecha a conexão
    conexao.close()
    print("Cliente atualizado com sucesso!")

    print("-" * 50)

while True:
    
    selecao = input("""
                    [1] Adicionar clientes
                    [2] Exibir tabela clientes
                    [3] Deletar ciente 
                    [4] Editar cliente
                    [5] Sair
                    Digite a opção:  """)
    
    print("-" * 50)

    if selecao == "1":
        add_clientes()

    elif selecao == "2":
        exibir_clientes()

    elif selecao == "3":
        id_para_deletar = input("Digite o id do cliente que deseja deletar: ")
        delete_cliente(id_para_deletar)

    elif selecao == "4":
        id_para_alterar = input("Digite o ID do cliente a ser alterado: ")
        print("*" * 50)
        cursor.execute(f'SELECT * FROM clientes WHERE id = {id_para_alterar}')
        cliente_alterando = cursor.fetchone()  # Recupera o primeiro registro para mostrar os dados no print. 

        if cliente_alterando:
            print("Você está alterando estes dados:")
            print(cliente_alterando)
            print("*" * 50)
            editar_cliente(id_para_alterar)

        else:
            print("Cliente não encontrado.")
            print("*" * 50)
    elif selecao == "5":
        break

# Fecha a conexão
conexao.close()
