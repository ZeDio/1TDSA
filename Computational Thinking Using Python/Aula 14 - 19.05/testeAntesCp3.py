'''
- Manipulação de listas com funções 
- Documentação docStrings

1) Função para definir o tamanho da lista
2) Função para criar e preencher a lista 
3) Função para percorrer e imprimir os elementos da lista
4) Função para somar todos os elementos da lista
5) Função para imprimir os pares da lista 
6) Função para imprimir os ímpares da lista
7) Função para retornar os elementos pares 
8) Função principal para testar o programa
'''

def tamanhoLista():
    tamanho = int(input("Insisa o tamanho da lista: "))
    return tamanho
def criarLista(tamanho):
    lista = []
    i = 0
    while i < tamanho:
        item = float(input("Digite item da lista: "))
        lista.append(item)
        i+=1
    return lista
def imprimir(lista):
    for item in lista:
        print(f"Item lista: {item}")
def somarLista(lista):
    soma = 0
    for item in lista:
        soma += item
    return soma
def imprimirPares(lista):
    for item in lista:
        if (item%2 == 0):
            print(f"O item {item} é par")
def imprimirImpar(lista):
    for item in lista:
        if (item%2 == 1):
            print(f"O item {item} é impar")

# Main
tamanho = tamanhoLista()
lista = criarLista(tamanho)
imprimir(lista)
somarLista(lista)
imprimirPares(lista)
imprimirImpar(lista)