import random
import time 

def arquivo():
    escolha = input("Deseja criar um arquvio ou acesalo\n"
    "- Criar\n"
    "- Abrir\n"
    "Digite sua resposta: ")

    while True:
        if escolha in ["criar", "CRIAR", "Criar", "C", "c"]:
            print("\n--- Criando Arquivo")
            nome_arquivo = input("\nColoque o nome do arquivo: ")
            arquivo_num = f"./{nome_arquivo}.txt"
            return arquivo_num
        elif escolha in ["abrir", "Abrir", "ABRIR", "A", "a"]:
            nome_arquivo = input("\nColoque o nome do arquivo que deseja abrir: ")
            arquivo_num = f"./{nome_arquivo}.txt"
            return arquivo_num
        else:
            print("Opção inexistente.. Digite novamente")
            return False

def lista(arquivo_num):
    while True:
        print(f"\n--- Definir Tamanho Da Lista ---"
              f"\n"
              f"1- 1000\n"
              f"2- 5000\n"
              f"3- 10000\n"
              f"4- 50000\n"
              f"5- Ler Lista")
        opcao_lista = int(input("Escolha uma opção: "))

        match opcao_lista:
            case 1:
                print("\n--- Lista com 1000 números")
                with open(arquivo_num, "w") as arquivo:
                    for i in range(1000):
                        numero = random.randint(1, 1000)
                        if i < 999:
                            arquivo.write(f"{numero},")
                        else:
                            arquivo.write(f"{numero}")
                ver_lista = input("Deseja ver a lista (S - N): ")
                if ver_lista in ["s", "S", "SIM", "Sim", "sim"]:
                    print(f"\n--- Ver Lista ---")
                    with open(arquivo_num, "r") as arquivo:
                        numero = arquivo.readlines()
                        for linha in numero:
                            print(linha.strip())
                ver_lista = None
                return arquivo_num
            case 2:
                print(f"\n--- Lista com 5000 números")
                with open(arquivo_num, "w") as arquivo:
                    for i in range(5000):
                        numero = random.randint(1, 5000)
                        if i < 4999:
                            arquivo.write(f"{numero},")
                        else:
                            arquivo.write(f"{numero}")
                ver_lista = input("Deseja ver a lista (S - N): ")
                if ver_lista in ["s", "S", "SIM", "Sim", "sim"]:
                    print(f"\n--- Ver Lista ---")
                    with open(arquivo_num, "r") as arquivo:
                        numero = arquivo.readlines()
                        for linha in numero:
                            print(linha.strip())
                ver_lista = None
                return arquivo_num
            case 3:
                print(f"\n--- Lista com 10000 números")
                with open(arquivo_num, "w") as arquivo:
                    for i in range(10000):
                        numero = random.randint(1, 10000)
                        if i < 9999:
                            arquivo.write(f"{numero},")
                        else:
                            arquivo.write(f"{numero}")
                ver_lista = input("Deseja ver a lista (S - N): ")
                if ver_lista in ["s", "S", "SIM", "Sim", "sim"]:
                    print(f"\n--- Ver Lista ---")
                    with open(arquivo_num, "r") as arquivo:
                        numero = arquivo.readlines()
                        for linha in numero:
                            print(linha.strip())
                ver_lista = None
                return arquivo_num
            case 4:
                print(f"\n--- Lista com 50000 números")
                with open(arquivo_num, "w") as arquivo:
                    for i in range(50000):
                        numero = random.randint(1, 50000)
                        if i < 49999:
                            arquivo.write(f"{numero},")
                        else:
                            arquivo.write(f"{numero}")
                ver_lista = input("Deseja ver a lista (S - N): ")
                if ver_lista in ["s", "S", "SIM", "Sim", "sim"]:
                    print(f"\n--- Ver Lista ---")
                    with open(arquivo_num, "r") as arquivo:
                        numero = arquivo.readlines()
                        for linha in numero:
                            print(linha.strip())
                ver_lista = None
                return arquivo_num
            case 5:
                print(f"\n--- Ver Lista ---")
                with open(arquivo_num, "r") as arquivo:
                    numero = arquivo.readlines()
                    for linha in numero:
                        print(linha.strip())
                return False, arquivo_num

def bubble_sort(lista):
    tam = len(lista)
    for i in range(tam - 1):
        troca = False
        for j in range(0, tam - i - 1):
            if lista[j] > lista[j + 1]:
                troca = True
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        if troca == False:
            return

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

def salvar_times(lista_das_listas, escolha, tempo):
    match escolha:
        case 1:
            lista_das_listas["lista_temp_bubble"].append(tempo)
        case 2:
            lista_das_listas["lista_temp_selection"].append(tempo)
        case 3:
            lista_das_listas["lista_temp_insertion"].append(tempo)
        case 4:
            lista_das_listas["lista_temp_merge"].append(tempo)

    return lista_das_listas

def dados(lista_das_listas):
    print(f"\n--- Dados Salvos \n")

    lista_temp_bubble = lista_das_listas["lista_temp_bubble"]
    lista_temp_selection = lista_das_listas["lista_temp_selection"]
    lista_temp_insertion = lista_das_listas["lista_temp_insertion"]
    lista_temp_merge = lista_das_listas["lista_temp_merge"]

     # Isso eu pedi ajuda no GPT    *[f"{num:.3f}" for num in lista_temp_]*
    print("│-------------------------------------------------------------│")
    if lista_temp_bubble:
        print("│ Tempo de execução do Bubble Sort:", 
        [f"{num:.3f}" for num in lista_temp_bubble],
        "\n│-------------------------------------------------------------│") 
    if lista_temp_selection:
        print("│ Tempo de execução do Selection Sort:", 
        [f"{num:.3f}" for num in lista_temp_selection],
        "\n│-------------------------------------------------------------│")
    if lista_temp_insertion:
        print("│ Tempo de execução do Insertion Sort:", 
        [f"{num:.3f}" for num in lista_temp_insertion],
        "\n│-------------------------------------------------------------│")
    if lista_temp_merge:
        print("│ Tempo de execução do Merge Sort:", 
        [f"{num:.3f}" for num in lista_temp_merge])
    print("│-------------------------------------------------------------│")

def algoritimos(lista_das_listas, arquivo_num):
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
            case 1:
                escolha = 1
                print(f"\n--- Organizando com Bubble Sort")
                with open(arquivo_num, "r") as arquivo:
                    conteudo = arquivo.read()

                lista = [int(num.strip()) for num in conteudo.split(",")]
                print(f"\nLista original: {lista}")
                inicio = time.time()
                bubble_sort(lista)
                fim = time.time()
                print(f"\nLista ordenada: {lista}")
                tempo = fim - inicio
                print(f'\nTempo para realizar: {tempo :.3f}')
                salvar_times(lista_das_listas, escolha, tempo)
                return
            case 2:
                escolha = 2
                print(f"\n--- Organizando com Selection Sort")
                with open(arquivo_num, "r") as arquivo:
                    conteudo = arquivo.read()

                lista = [int(num.strip()) for num in conteudo.split(",")]
                print(f"\nLista original: {lista}")
                inicio = time.time()
                selection_sort(lista)
                fim = time.time()
                print(f"\nLista ordenada: {lista}")
                tempo = fim - inicio
                print(f'\nTempo para realizar: {tempo :.3f}')
                salvar_times(lista_das_listas, escolha, tempo)
                return
            case 3:
                escolha = 3
                print(f" --- Organizando com Insertion Sort")
                with open(arquivo_num, "r") as arquivo:
                    conteudo = arquivo.read()

                lista = [int(num.strip()) for num in conteudo.split(",")]
                print(f"Lista original: {lista}")
                inicio = time.time()
                insertion_sort(lista)
                fim = time.time()
                print(f"Lista ordenada: {lista}")
                tempo = fim - inicio
                print(f'\nTempo para realizar: {tempo :.3f}')
                salvar_times(lista_das_listas, escolha, tempo)
                return
            case 4:
                escolha = 4
                print(f"\n--- Organizando com Merge Sort")
                with open(arquivo_num, "r") as arquivo:
                    conteudo = arquivo.read()

                lista = [int(num.strip()) for num in conteudo.split(",")]
                print(f"\nLista original: {lista}")
                inicio = time.time()
                merge_sort(lista)
                fim = time.time()
                print(f"\nLista ordenada: {lista}")
                tempo = fim - inicio
                print(f'\nTempo para realizar: {tempo :.3f}')
                salvar_times(lista_das_listas, escolha, tempo)
                return
            case 5:
                print(f"\n--- Saindo dos Algoritimos")
                return False

def main():
    lista_das_listas = {
        "lista_temp_bubble": [],
        "lista_temp_selection": [],
        "lista_temp_insertion": [],
        "lista_temp_merge": []
    }

    print(f"\n--- Bem Vindo Ao Sistema ---\n")
    arquivo_num = arquivo()

    while True:
        print(f"\n--- Menu Do Sistema ---"
              f"\n"
              f"1- Tamanho da Lista\n"
              f"2- Algoritimos de Ordenação\n"
              f"3- Dados Salvos\n"
              f"4- Sair do Progama")
        opcao_menu = int(input("Escolha uma opção: "))

        match opcao_menu:
            case 1:
                lista(arquivo_num)
            case 2:
                algoritimos(lista_das_listas, arquivo_num)
            case 3:
                dados(lista_das_listas)
            case 4:
                print("Saindo do sistema... Até logo!")
                return False

#Codigo Principal..
main()