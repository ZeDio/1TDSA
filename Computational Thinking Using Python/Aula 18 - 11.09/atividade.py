'''

'''
import oracledb

def getConnection():
    try:
        conn = oracledb.connect(
            user = "rm562341",
            password = "100407",
            host = "oracle.fiap.com.br",
            port = "1521",
            service_name = "orcl"
            #dominio = dominio
        )
        print('Conexão com Oracle DB realizada!')
    except Exception as e:
        print(f'Erro ao obter a conexão: {e}')
    return conn

def create_table(conn):
    cursor = conn.cursor()

    try:
        sql = """
            CREATE TABLE produtos(
            id number GENERATED ALWAYS AS IDENTITY,
            nome VARCHAR(30),
            descricao VARCHAR(30),
            fornecedor VARCHAR(30),
            preco float(10),
            PRIMARY KEY (id)
            )
        """
        cursor.execute(sql)
        print(f'Tabela produtos foi criada com sucesso!')
    except oracledb.Error as e:
        print(f'Erro de conexão: {e}')


#Operações CRUD
def create_produto(nome, descricao, fornecedor, preco):
    print('*** Inserindo um novo Produto na tabela produtos ***')
    conn = getConnection()

    #validação da conexão
    if not conn:
        return
    
    try:
        cursor = conn.cursor() #obter um cursor
        sql = """
            INSERT INTO produtos (nome, descricao, fornecedor, preco)
            VALUES (:nome, :descricao, :fornecedor, :preco)
        """
        cursor.execute(sql, {
            'nome' : nome,
            'descricao' : descricao,
            'fornecedor' : fornecedor,
            'preco' : preco
        })
        conn.commit()
        print(f'Produto {nome}, {descricao} adicionado com sucesso!')
    except oracledb.Error as e:
        print(f'\nErro ao inserior Produto: {e}')
        conn.rollback()
    finally:
        if conn:
            conn.close()    

#Exibir os dados de todos os Produtos
def read_produtos():
    print('*** Lê e exibe todos os Produtos da tabela ***')
    conn = getConnection()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        sql = """
            SELECT * FROM produtos ORDER BY id
        """
        cursor.execute(sql)
        print("\n --- Lista de Produtos ---")
        rows = cursor.fetchall()
        for row in rows:
            print(f'ID: {row[0]}, Nome: {row[1]} {row[2]}, Empresa: {row[3]}, Idade: {row[4]}')
            print('----------------------------------')
    except oracledb.Error as e:
        print(f'\nErro ao ler Produtos: {e}')
    finally:
        if conn:
            conn.close()
 
#Atualizar algum Produto pelo ID
def update_produto(id, new_preco):
    print(f'*** Atualizado o valor de um Produto com base no ID ***')
    conn = getConnection()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        sql = "UPDATE produtos SET preco = :new_preco WHERE id = :id"
        cursor.execute(sql, {'new_preco' : new_preco, 'id' : id} )
        conn.commit()
        if cursor.rowcount > 0:
            print(f'Preço do Produto com ID {id} foi atualizado!')
        else:
            print(f'Nenhum Produto com ID {id} foi encontrado!')
    except oracledb.Error as e:
        print(f'\nErro ao atualizar o preço: {e}')
        conn.rollback()
    finally:
        if conn:
            conn.close()


#Remover o CEO pelo ID
#Delete
def delete_produto(id):
    print(f'*** Deletar um Produto pelo ID: {id} ***')
    conn = getConnection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        sql = "DELETE FROM produtos WHERE id= :id"
        cursor.execute(sql, {'id':id})
        conn.commit()
        if cursor.rowcount > 0:
            print(f'Produto com id: {id}, foi excluido com sucesso!')
        else:
            print(f'Nenhum Produto foi deletado com o id: {id}')
    except oracledb as e:
        print(f'\nrro ao Excluir Produto')
        conn.rollback()
    finally:
        if conn:
            conn.close()

#Programa Principal
conn = getConnection()
print(f'Conexão: {conn.version}')
create_table(conn)

while True:
    print('\nOlá, você vai entrar em um sistema de Produtos..\n'
          'A seguir, escolha uma opção para fazer alguma movimentação no sistema..\n\n'
          '1 - Cadastrar um novo produto\n'
          '2 - Ver produtos cadastrados\n'
          '3 - Fazer um Update em algum produto\n'
          '4 - Deletar algum produto\n'
          '5 - Sair do programa\n')
    try:
        escolha = int(input('Digite o que deseja realizar..: '))
    except ValueError:
        print("Digite apenas números de 1 a 5.")
        continue

    if escolha == 1:
        print("Cadastrar produto...\n\n")
        nome = input('Digite o nome do produto..: ')
        descricao = input('\nDigite o descrição do produto..: ')
        marca = input('\nDigite o marca do produto..: ')
        preco = int(input('\nDigite o valor do produto..: '))
        create_produto(nome, descricao, marca, preco)
        read_produtos()
    elif escolha == 2:
        print("Listar produtos...\n\n")
        read_produtos()
    elif escolha == 3:
        print("Atualizar produto...\n\n")
        id = input('Digite o id do produto..: ')
        preco = int(input('\nDigite o valor do produto..: '))
        update_produto(id,preco)
        read_produtos()
    elif escolha == 4:
        print("Deletar produto...\n\n")
        id = input('Digite o id do produto..: ')
        delete_produto(id)
        read_produtos()
    elif escolha == 5:
        print("Saindo do programa... Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")