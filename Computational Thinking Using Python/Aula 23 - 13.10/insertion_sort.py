'''
Algoritimo Insertion Sort (Ordenação por inserção)
- Complexidade: O(n²)
'''
import time 

def insertion_sort(lista):
    #função de ordenação Insertion Sort
    n = len(lista)

    for i in range(1,n):
        pivo = lista[i]
        j = i-1
        while j >= 0 and pivo < lista[j]:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = pivo

def soma(lista):
    total = 0
    for i in lista:
        total += i
    return total

#Progama Principal
lista = [12, 11, 13, 5, 6]
print(f'\nLista Original: {lista}\n')
incio = time.time()
insertion_sort(lista)
fim = time.time()
print(f'Lista Ordenada: {lista}')
print(f'Tempo: {fim - incio}')
print(f'Total da Soma: {soma(lista)}')