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
    '''
    Obter e retornar um número inteiro - tamanho da lista
    
    Parâmetros:
    - não tem parâmetros

    Retorno: 
    - retorna um número inteiro - representando o tamanho da lista
    '''
    print('--- Tamanho da lista ---')
    print('------------------------')
    n = int(input("Tamanho: "))
    return n 

def criarLista(t):
    print(f'--- Criando uma lista com {t} elementos ---')
    print('--------------------------------------------')
    lista = [] # lista vazia
    i = 0 # variável de controle

    #preechendo a lista
    while i < t: 
        n = int(input("Número: "))
        lista.append(n)
        i+=1
    return lista

def imprimir(lista):
    print('--- Imprimindo a lista ---')
    print('--------------------------')
    for n in lista: 
        print(f'Número: {n}')

def somarElementos(lista):
    print('--- Somando os elementos da lista ---')
    print('-------------------------------------')
    soma = 0 
    for n in lista:
        soma += n
    return soma 

def subtrairElementos(lista): 
    print('--- Subtraindo os elementos da lista ---')
    print('----------------------------------------')
    subtracao = 0
    for n in lista:
        subtracao -= n
    print(f'Subtração: {subtracao}')
    return subtracao

def numerosPares(lista): 
    print('--- Números pares ---')
    print('---------------------')
    for n in lista: 
      if n % 2 == 0: 
        print(f'{n} é par')

def numerosImpares(lista): 
    print('--- Números ímpares ---')
    print('-----------------------')
    for n in lista: 
      if n % 2 == 1: 
        print(f'{n} é ímpar')


#Principal - (main)
print('-----------------')
print('--- Principal ---')
t = tamanhoLista()
lista = criarLista(t)
imprimir(lista)
print(f'Soma: {somarElementos(lista)}')
subtrairElementos(lista)
numerosPares(lista)
numerosImpares(lista)