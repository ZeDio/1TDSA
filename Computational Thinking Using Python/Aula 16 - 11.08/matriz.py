"""
1 - Função para criar uma matriz (Lista de listas)
2 - Função que recebe a matriz numérica por parâmetro e retorna a soma de todos os elementos da matriz
3 - Função para imprimir a soma dos elementos da matriz
"""

def definir_ns():
    n_linhas = int(input("Digite o numero de linhas: "))
    n_colunas = int(input("Digite o numero de colunas: "))
    return n_linhas, n_colunas

def criar_matriz(n_linhas, n_colunas):
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            n = int(input("Insira o numero: "))
            linha.append(n)

        matriz.append(linha)
    return matriz

def soma_matriz(matriz):
    total = 0
    for i in matriz:
        for j in i:
            total += j
    return total

def main():
    n_linhas, n_colunas = definir_ns()
    matriz = criar_matriz(n_linhas, n_colunas)
    total = soma_matriz(matriz)
    print(f"O total da soma da matriz é: {total}")

main()