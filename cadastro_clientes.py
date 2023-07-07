import sqlite3

conexao = sqlite3.connect('cadastro_clientes.db')
cursor = conexao.cursor()

# Cria a tabela
# cursor.execute('CREATE TABLE clientes (id INT, nome VARCHAR(45), idade INT, endereco VARCHAR(50), telefone VARCHAR(15))')
def exibir_clientes():
    # Executa a consulta SELECT
    cursor.execute('SELECT * FROM clientes')

    # Recupera todos os registros
    registros = cursor.fetchall()

    # Exibe os registros
    for registro in registros:
        print(registro)

def add_clientes():
    codigo_cliente = input("Digite o código do cliente: ")
    nome_cliente = input("Digite o nome do cliente: ")
    idade_cliente = input("Digite a idade do cliente: ")
    endereco_do_cliente = input("Digite o endereço do cliente: ")
    telefone_do_cliente = input("Digite o telefone do cliente: ")

    cursor.execute('INSERT INTO clientes VALUES(?,?,?,?,?)', (codigo_cliente, nome_cliente, idade_cliente, endereco_do_cliente, telefone_do_cliente))

    # Confirma as alterações
    conexao.commit()

    print("Cliente adicionado com sucesso!")

while True:
    selecao = input("Digite a opção [1] Adicionar clientes [2] Exibir tabela clientes [7] Sair: ")

    if selecao == "1":
        add_clientes()

    elif selecao == "2":
        exibir_clientes()

    elif selecao == "7":
        break

# Fecha a conexão
conexao.close()
