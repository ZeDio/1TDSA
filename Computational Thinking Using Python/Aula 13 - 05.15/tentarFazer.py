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

def tamanhoLista(): #1) Função para definir o tamanho da lista
    numero = int(input('tamanho da lista:'))
    print(f"tamanho da lista definido - {numero}")
    print("------------------------------------")
    return numero

def criarLista(numero): #2) Função para criar e preencher a lista 
    lista = []
    i = 0
    while i < numero:
        valor = float(input('Digite o valor para adicionar na lista:'))
        lista.append(valor) 
        i+=1
    print("------------------------------------")
    return lista

def imprimir(lista): #3) Função para percorrer e imprimir os elementos da lista
    for item in lista:
        print(item)
    print("------------------------------------")

def somarLista(lista):#4) Função para somar todos os elementos da lista
    soma = 0
    for item in lista:
        soma += item
    return soma

def imprimirImparesLista(lista): #6) Função para imprimir os ímpares da lista
    for item in lista:
        if (item%2 == 1):
            print(item)
    print("------------------------------------")

def imprimirParesLista(lista): #7) Função para retornar os elementos pares 
    for item in lista:
        if (item%2 == 0):
            print(item)
    print("------------------------------------")

#8) Progama Principal
numero = tamanhoLista()
lista = criarLista(numero)
imprimir(lista)
print(f"Soma dos elementos da lista: {somarLista(lista)}")
print("------------------------------------")
imprimirImparesLista(lista)
imprimirParesLista(lista)