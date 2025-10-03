import os

ARQUIVO_TEXTO = "./inventario.txt"

# Função auxiliar para ler todos os produtos em lista
def ler_todos():
    try:
        with open(ARQUIVO_TEXTO, "r") as arquivo:
            linhas = [linha.strip() for linha in arquivo.readlines()]
        return linhas
    except FileNotFoundError:
        return []


# CREATE - Adicionar produto
def adicionar_produto(nome, preco, quantidade):
    with open(ARQUIVO_TEXTO, "a") as arquivo:
        arquivo.write(f"{nome},{preco},{quantidade}\n")
    print(f"[OK] Produto '{nome}' adicionado com sucesso.")


# READ - Listar produtos (com busca opcional)
def listar_produtos(busca=None):
    produtos = ler_todos()
    if not produtos:
        print("Inventário vazio.")
        return

    print("\n--- Inventário ---")
    for produto in produtos:
        nome, preco, qtd = produto.split(",")
        if not busca or busca.lower() in nome.lower():
            print(f"Nome: {nome} | Preço: R${preco} | Quantidade: {qtd}")


# UPDATE - Atualizar produto pelo nome
def atualizar_produto(nome_alvo, novo_preco=None, nova_qtd=None):
    produtos = ler_todos()
    atualizado = False

    with open(ARQUIVO_TEXTO, "w") as arquivo:
        for produto in produtos:
            nome, preco, qtd = produto.split(",")
            if nome.lower() == nome_alvo.lower():
                if novo_preco is not None:
                    preco = str(novo_preco)
                if nova_qtd is not None:
                    qtd = str(nova_qtd)
                atualizado = True
            arquivo.write(f"{nome},{preco},{qtd}\n")

    if atualizado:
        print(f"[OK] Produto '{nome_alvo}' atualizado com sucesso.")
    else:
        print(f"[ERRO] Produto '{nome_alvo}' não encontrado.")


# DELETE - Remover produto pelo nome
def remover_produto(nome_alvo):
    produtos = ler_todos()
    removido = False

    with open(ARQUIVO_TEXTO, "w") as arquivo:
        for produto in produtos:
            nome, preco, qtd = produto.split(",")
            if nome.lower() != nome_alvo.lower():
                arquivo.write(produto + "\n")
            else:
                removido = True

    if removido:
        print(f"[OK] Produto '{nome_alvo}' removido com sucesso.")
    else:
        print(f"[ERRO] Produto '{nome_alvo}' não encontrado.")


# Menu de operações
def menu():
    while True:
        print("\n=== SISTEMA DE INVENTÁRIO ===")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Remover Produto")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            qtd = int(input("Quantidade: "))
            adicionar_produto(nome, preco, qtd)

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            nome = input("Nome do produto que deseja atualizar: ")
            novo_preco = input("Novo preço (ou Enter para manter): ")
            nova_qtd = input("Nova quantidade (ou Enter para manter): ")

            atualizar_produto(
                nome,
                float(novo_preco) if novo_preco else None,
                int(nova_qtd) if nova_qtd else None,
            )

        elif opcao == "4":
            nome = input("Nome do produto que deseja remover: ")
            remover_produto(nome)

        elif opcao == "5":
            print("Saindo do sistema... Até logo!")
            break

        else:
            print("[ERRO] Opção inválida! Tente novamente.")


#Principal
    menu()