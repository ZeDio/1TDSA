#Algoritimo Bubble Sort
#Complexodade: O(n²)

def bubble_sort(sequencia):
    tamanho = len(sequencia)

    for i in range( tamanho - 1 ):
        troca = False #flag de controle
        for j in range(0, tamanho - i - 1):
            if sequencia[j] > sequencia[j+1]:
                troca = True
                sequencia[j], sequencia[j+1] = sequencia[j+1], sequencia[j] #atribuição paralela
        # se não for necessário realizar a troca, o progama irá ira sair do loop
        if not troca: # ou if troca == False:  
            return 
        
#Progama Principal
lista = [3,1,7,2,4,6,5]
print(f"A seguinte lista sem está arrumada..: {lista}")
bubble_sort(lista) #Função com efeito colateral
print(f"Lista ordenada: {lista}")