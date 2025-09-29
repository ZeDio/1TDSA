'''
Manipulação de dados em Arquivos texto
Pensamento Computacional

-Decomposição em 3 etapas:
    1. Abertura do Arquivo
    2. Procesamento de dados (Escrever e Ler)
    3. Fechamento do Arquivo

Em Python, essas operações ocorrem através de duas funções
    - open() - lida com a etapa 1
        Modos de operação:
            - "w" (write - escrita) - Cria um arquivo novo, permitindo a escrita... 
              obs: se o arquivo já existir, todo o seu conteúdo será apagado e um novo arquivo será criado.
            - "r" (read - leitura) - Abre o arquivo  já existente apenas para leitura.
            - "a" (append - adicionar) - Abre o arquivo para escrita, adicionando 
              um novo item(elemento) ao final do arquivo.
            - Abertura com with - Permite que o arquivo seja automaticamente fechado, ao término da operação.
    - .close() - Método que fecha o arquivo - lida com a etapa 3
'''

#Exemplo prático de persistência de dados em Arquivos Texto
#Cadastro de nomes de alunos

import os

"""
Escrever uma lista de strings (Nomes de alunos) em um arquivo
sobrescrever os dados existentes ("w")
"""

ARQUIVO_TEXTO = 'cadastro.txt'

def escrever(dados):
    print(">>> Escrevendo no Arquivo...")
    try:
        """
        with permite que o arquivo seja fechado através da abstração,
        escondendo a complexidade do gerenciamento de recursos
        """
        with open(ARQUIVO_TEXTO, "w") as arquivo:
            for item in dados:
                arquivo.write(f'{item}\n')
        print(f'\n [Sucesso] Dados escritos em {ARQUIVO_TEXTO}')
    except Exception as e:
        print(f'[Erro] Ocorreu um erro ao escrever no arquivo: {e}')


"""
Leitura de todas as linhas de um Arquivo, retornando como uma lista
"""
def ler():
    print(">>> Lendo dados do Arquivo...")
    try: 
        with open(ARQUIVO_TEXTO, "r") as arquivo:
            linhas = []
            for linha in arquivo.readlines():
                #remove os espaços em brancos e quebra linhas = .strip
                linhas.append(linha.strip())
            return linhas
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f'[Erro] Ocorreu um erro: {e}')
        return []

"""
Adicionar uma nova string ao final do arquivo
"""

def adicionar(novo_dado):
    print(">>> Adicionando um novo dado ao final Arquivo...")
    try:
        with open(ARQUIVO_TEXTO, "a") as arquivo:
            arquivo.write(f'{novo_dado}\n')
        print(f'\n [Sucesso] {novo_dado} foi inserido no Arquivo')
    except Exception as e:
        print(f'[Erro] Ocorreu um erro: {e}')

"""
Exibe o menu de opções para o usuário e processa as informações
"""

def menu():
    print(">>> Menu de Operações <<<")
    while True:
        print("\n --- Persistênsia de Dados Em Arquivos ---" \
        "\n1. Escrever no Arquivo" \
        "\n2. Ler o Arquivo" \
        "\n3. Adicionar no Arquivo" \
        "\n4. Sair")
        
        escolha = input("Escolha uma opção(1-4): ")

        if escolha == '1':
            dados_brutos = input("Digite os dados separado por virgula (ex. Ana,Bruno,Calor): ")
            dados = dados_brutos.split(',')
            dados_limpos = []
            for item in dados:
                dados_limpos.append(item.strip())
            escrever(dados_limpos)
        elif escolha == '2':
            ler()
        elif escolha == '3':
            dados_brutos = input("Digite os dados separado por virgula (ex. Ana,Bruno,Calor): ")
            dados = dados_brutos.split(',')
            dados_limpos = []
            for item in dados:
                dados_limpos.append(item.strip())
            adicionar(dados_limpos)   
        elif escolha == '4':
            break

#Progama Principal
menu()