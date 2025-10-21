import random
import os
import time 
lista_numeros = "./lista_numeros.txt"

def lista():
    while True:
        print(f"\n --- Definir Tamanho Da Lista ---"
              f"\n"
              f"1- 1000\n"
              f"2- 5000\n"
              f"3- 10000\n"
              f"4- 50000\n"
              f"5- Ler Lista")
        opcao_lista = int(input("Escolha uma opção: "))

        match opcao_lista:
            case 1:
                print("\n --- Lista com 1000 números")
                with open(lista_numeros, "w") as arquivo:
                    for i in range(1000):
                        numero = random.randint(1, 1000)
                        if i < 999:
                            arquivo.write(f"{numero},")
                        else:
                            arquivo.write(f"{numero}")
                return False
            case 2:
                print(f"\n --- Lista com 5000 números")
                with open(lista_numeros, "w") as arquivo:
                    for i in range(5000):
                        numero = random.randint(1, 5000)
                        if i < 4999:
                            arquivo.write(f"{numero},")
                        else:
                            arquivo.write(f"{numero}")
                return False
            case 3:
                print(f"\n --- Lista com 10000 números")
                with open(lista_numeros, "w") as arquivo:
                    for i in range(10000):
                        numero = random.randint(1, 10000)
                        if i < 9999:
                            arquivo.write(f"{numero},")
                        else:
                            arquivo.write(f"{numero}")
                return False
            case 4:
                print(f"\n --- Lista com 50000 números")
                with open(lista_numeros, "w") as arquivo:
                    for i in range(50000):
                        numero = random.randint(1, 50000)
                        if i < 49999:
                            arquivo.write(f"{numero},")
                        else:
                            arquivo.write(f"{numero}")
                return False
            case 5:
                print(f"\n--- Ver Lista ---")
                with open(lista_numeros, "r") as arquivo:
                    numero = arquivo.readlines()
                    for linha in numero:
                        print(linha.strip())
                return False

#Problema...
def bubble_sort(lista):
    tam = len(lista)
    for i in range(tam - 1):
        troca = False
        for j in range(0, tam - i - 1):
            if lista[j] > lista[j + 1]:
                troca = True
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            if not troca:
                return lista

def selection_sort(lista):
    tam = len(lista)
    for i in range(tam):
        indice_minimo = i
        for j in range(i + 1, tam):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

def insertion_sort(lista):
    tam = len(lista)
    for i in range(1, tam):
        ref = lista[i]
        j = i - 1
        while j >= 0 and ref < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = ref

def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2

        L = lista[:meio]
        R = lista[meio:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len((L)) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        while i < len((L)):
            lista[k] = L[i]
            i += 1
            k += 1

        while j < len((R)):
            lista[k] = R[j]
            j += 1
            k += 1
    return lista

def algoritimos():
    while True:
        print(f"\n--- Definir Algoritimo ---"
              f"\n"
              f"1- Bubble Sort\n"
              f"2- Selection Sort\n"
              f"3- Insertion Sort\n"
              f"4- Merge Sort\n"
              f"5- Sair")
        opcao_algoritimo = int(input("Escolha uma opção: "))

        match opcao_algoritimo:
            #Problema no Primeiro --> Case 1
            case 1:
                print(f"\n--- Organizando com Bubble Sort")
                with open(lista_numeros, "r") as arquivo:
                    conteudo = arquivo.read()

                lista = [int(num.strip()) for num in conteudo.split(",")]
                print(f"\nLista original: {lista}")
                incio = time.time()
                bubble_sort(lista)
                fim = time.time()
                print(f"\nLista ordenada: {lista}")
                print(f'\nTempo para realizar: {(fim - incio):.3f}')
                return

            case 2:
                print(f"\n--- Organizando com Selection Sort")
                with open(lista_numeros, "r") as arquivo:
                    conteudo = arquivo.read()

                lista = [int(num.strip()) for num in conteudo.split(",")]
                print(f"\nLista original: {lista}")
                incio = time.time()
                selection_sort(lista)
                fim = time.time()
                print(f"\nLista ordenada: {lista}")
                print(f'\nTempo para realizar: {(fim - incio):.3f}')
                return

            case 3:
                print(f" --- Organizando com Insertion Sort")
                with open(lista_numeros, "r") as arquivo:
                    conteudo = arquivo.read()

                lista = [int(num.strip()) for num in conteudo.split(",")]
                print(f"Lista original: {lista}")
                incio = time.time()
                insertion_sort(lista)
                fim = time.time()
                print(f"Lista ordenada: {lista}")
                print(f'\nTempo para realizar: {(fim - incio):.3f}')
                return

            case 4:
                print(f"\n--- Organizando com Merge Sort")
                with open(lista_numeros, "r") as arquivo:
                    conteudo = arquivo.read()

                lista = [int(num.strip()) for num in conteudo.split(",")]
                print(f"\nLista original: {lista}")
                incio = time.time()
                merge_sort(lista)
                fim = time.time()
                print(f"\nLista ordenada: {lista}")
                print(f'\nTempo para realizar: {(fim - incio):.3f}')
                return
            
            case 5:
                print(f"\n--- Saindo dos Algoritimos")
                return False

def main():
    while True:
        print(f"\n --- Menu Do Sistema ---"
              f"\n"
              f"1- Tamanho da Lista\n"
              f"2- Algoritimos de Ordenação\n"
              f"3- Dados Salvos\n"
              f"4- Sair do Progama")
        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                lista()
            case 2:
                algoritimos()
            case 3:
                print()
            case 4:
                print("Saindo do sistema... Até logo!")
                return False

#Codigo Principal..
main()