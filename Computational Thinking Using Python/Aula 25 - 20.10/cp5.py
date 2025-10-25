import random
import time 
import matplotlib.pyplot as plt

"""
O progama ele cria ou entra nas listas pre geradas
"""

# Função que cria ou abre um arquivo
def arquivo():
    while True:
        escolha = input("Deseja criar um arquvio ou acessá-lo\n"
        "- Criar\n"
        "- Abrir\n"
        "Digite sua resposta: ")

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
            print("\nOpção inexistente.. Digite novamente\n")

# Função que cria a lista
def criar_lista(arquivo_num, lista_das_listas):
    while True:
        print(f"\n--- Definir Tamanho Da Lista ---"
              f"\n"
              f"1- 1000\n"
              f"2- 5000\n"
              f"3- 10000\n"
              f"4- 25000\n"
              f"5- 50000\n"
              f"6- Ler Lista")
        opcao_lista = int(input("Escolha uma opção: "))

        match opcao_lista:
            case 1:
                print("\n--- Lista com 1000 números")
                lista_das_listas["lista_tamanho"].append("1000")
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
                return arquivo_num, lista_das_listas
            case 2:
                print(f"\n--- Lista com 5000 números")
                lista_das_listas["lista_tamanho"].append("5000")
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
                lista_das_listas["lista_tamanho"].append("10000")
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
                print(f"\n--- Lista com 25000 números")
                lista_das_listas["lista_tamanho"].append("25000")
                with open(arquivo_num, "w") as arquivo:
                    for i in range(25000):
                        numero = random.randint(1, 25000)
                        if i < 24999:
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
                print(f"\n--- Lista com 50000 números")
                lista_das_listas["lista_tamanho"].append("50000")
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
            case 6:
                print(f"\n--- Ver Lista ---")
                with open(arquivo_num, "r") as arquivo:
                    numero = arquivo.readlines()
                    for linha in numero:
                        print(linha.strip())
                return False, arquivo_num

# Função que executa o algoritimo bubble sort
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

# Função que executa o algoritimo selection sort
def selection_sort(lista):
    tam = len(lista)
    for i in range(tam):
        indice_minimo = i
        for j in range(i + 1, tam):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

# Função que executa o algoritimo insertion sort
def insertion_sort(lista):
    tam = len(lista)
    for i in range(1, tam):
        ref = lista[i]
        j = i - 1
        while j >= 0 and ref < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = ref

# Função que executa o algoritimo merge sort
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

# Função que salva o tempo de execução do algoritimo
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

# Função que exime os tempo dos algoritimos
def dados(lista_das_listas):
    print("\n--- Resultados dos Testes de Algoritmos ---\n")

    tamanhos = lista_das_listas.get("lista_tamanho", [])
    bubble = lista_das_listas.get("lista_temp_bubble", [])
    selection = lista_das_listas.get("lista_temp_selection", [])
    insertion = lista_das_listas.get("lista_temp_insertion", [])
    merge = lista_das_listas.get("lista_temp_merge", [])

    if not tamanhos:
        print("Nenhum dado disponível para gerar a tabela.")
        return

    # Agrupar tempos por tamanho de lista
    dados_agregados = {}
    for i, n in enumerate(tamanhos):
        if n not in dados_agregados:
            dados_agregados[n] = {
                "Bubble Sort": [],
                "Selection Sort": [],
                "Insertion Sort": [],
                "Merge Sort": []
            }

        if i < len(bubble):
            dados_agregados[n]["Bubble Sort"].append(bubble[i])
        if i < len(selection):
            dados_agregados[n]["Selection Sort"].append(selection[i])
        if i < len(insertion):
            dados_agregados[n]["Insertion Sort"].append(insertion[i])
        if i < len(merge):
            dados_agregados[n]["Merge Sort"].append(merge[i])

    # Definir colunas (nome e largura mínima)
    colunas = [
        ("Algoritmo", 14),
        ("N", 8),
        ("Amostra 1 (s)", 12),
        ("Amostra 2 (s)", 12),
        ("Amostra 3 (s)", 12),
        ("Média (s)", 10)
    ]

    # Reunir todas as linhas de dados (como strings) para calcular larguras reais
    linhas_dados = []
    for n, algs in dados_agregados.items():
        for alg_nome in ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort"]:
            tempos = algs[alg_nome][:3]  # até 3 amostras
            tempos_fmt = [f"{t:.3f}" for t in tempos]
            while len(tempos_fmt) < 3:
                tempos_fmt.append("-")
            media = f"{(sum(tempos)/len(tempos)):.3f}" if tempos else "-"
            linha = [
                alg_nome,
                str(n),
                tempos_fmt[0],
                tempos_fmt[1],
                tempos_fmt[2],
                media
            ]
            linhas_dados.append(linha)

    # Ajustar largura de cada coluna com base no maior conteúdo (cabeçalho ou dados)
    larguras = []
    for idx, (titulo, largura_min) in enumerate(colunas):
        maior = len(titulo)
        for linha in linhas_dados:
            maior = max(maior, len(str(linha[idx])))
        larguras.append(max(largura_min, maior))

    # Função para montar uma linha formatada usando as larguras calculadas
    def montar_linha(celulas):
        parts = []
        for i, cell in enumerate(celulas):
            w = larguras[i]
            parts.append(f" {str(cell):<{w}} ")
        # juntar com '│' e garantir que comece e termine com '│'
        return "│" + "│".join(parts) + "│"

    # Montar cabeçalho
    cabecalho = [c[0] for c in colunas]
    linha_cabecalho = montar_linha(cabecalho)

    # Usar o comprimento da linha de cabeçalho para criar as bordas exatamente do mesmo tamanho
    inner_len = len(linha_cabecalho) - 2  # menos os cantos
    linha_topo = "┌" + "─" * inner_len + "┐"
    linha_meio = "├" + "─" * inner_len + "┤"
    linha_fundo = "└" + "─" * inner_len + "┘"

    # Imprimir tabela
    print(linha_topo)
    print(linha_cabecalho)
    print(linha_meio)

    # Imprimir linhas agrupadas por N (para manter ordem previsível, ordenamos tamanhos)
    for n in sorted(dados_agregados.keys(), key=lambda x: (int(x) if str(x).isdigit() else x)):
        algs = dados_agregados[n]
        for alg_nome in ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort"]:
            tempos = algs[alg_nome][:3]
            tempos_fmt = [f"{t:.3f}" for t in tempos]
            while len(tempos_fmt) < 3:
                tempos_fmt.append("-")
            media = f"{(sum(tempos)/len(tempos)):.3f}" if tempos else "-"
            linha = [alg_nome, str(n), tempos_fmt[0], tempos_fmt[1], tempos_fmt[2], media]
            print(montar_linha(linha))
        # separador entre blocos de N
        print(linha_meio)

    print(linha_fundo)
# Função que gera a tabela dos resultados
def gerar_tabela(lista_das_listas):
    # Extrai os dados das listas
    tamanhos = [int(t) for t in lista_das_listas["lista_tamanho"]]
    tempos_bubble = lista_das_listas["lista_temp_bubble"]
    tempos_selection = lista_das_listas["lista_temp_selection"]
    tempos_insertion = lista_das_listas["lista_temp_insertion"]
    tempos_merge = lista_das_listas["lista_temp_merge"]

    # Verifica se há dados
    if not tamanhos:
        print("\nNenhum dado disponível para gerar a tabela.")
        return

    # Organiza dados por algoritmo, tamanho e amostras
    dados_organizados = {}
    
    # Para cada algoritmo, agrupa os tempos por tamanho
    algoritmos = {
        "Bubble Sort": tempos_bubble,
        "Selection Sort": tempos_selection,
        "Insertion Sort": tempos_insertion,
        "Merge Sort": tempos_merge
    }
    
    for nome_algo, tempos in algoritmos.items():
        if nome_algo not in dados_organizados:
            dados_organizados[nome_algo] = {}
        
        for i, tamanho in enumerate(tamanhos):
            if i < len(tempos):
                if tamanho not in dados_organizados[nome_algo]:
                    dados_organizados[nome_algo][tamanho] = []
                dados_organizados[nome_algo][tamanho].append(tempos[i])
    
    # Prepara os dados para a tabela
    col_labels = ['Algoritmo', 'N', 'Amostra 1 (s)', 'Amostra 2 (s)', 'Amostra 3 (s)', 'Tempo Médio (s)']
    tbl_data = []
    
    # Ordena algoritmos e tamanhos para exibição organizada
    for algoritmo in sorted(dados_organizados.keys()):
        tamanhos_ordenados = sorted(dados_organizados[algoritmo].keys())
        
        for tamanho in tamanhos_ordenados:
            amostras = dados_organizados[algoritmo][tamanho]
            
            # Preenche até 3 amostras (se não houver 3, preenche com '-')
            amostra1 = f"{amostras[0]:.3f}" if len(amostras) > 0 else "-"
            amostra2 = f"{amostras[1]:.3f}" if len(amostras) > 1 else "-"
            amostra3 = f"{amostras[2]:.3f}" if len(amostras) > 2 else "-"
            
            # Calcula a média apenas das amostras disponíveis
            media = sum(amostras) / len(amostras) if amostras else 0
            media_str = f"{media:.3f}" if amostras else "-"
            
            linha = [algoritmo, str(tamanho), amostra1, amostra2, amostra3, media_str]
            tbl_data.append(linha)
    
    # Verifica se há dados para exibir
    if not tbl_data:
        print("\nNenhum dado disponível para gerar a tabela.")
        return
    
    # Criação da tabela
    fig, ax = plt.subplots(figsize=(14, len(tbl_data) * 0.4 + 1.5))
    ax.axis('tight')
    ax.axis('off')
    
    table = ax.table(cellText=tbl_data, colLabels=col_labels, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.8)
    
    plt.title("Tabela de Resultados: Tempos de Execução dos Algoritmos de Ordenação", 
              fontsize=13, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.show()
#Essas duas funções basicamente fazem a mesma coisa...

# Função escolhe qual algoritimo vai ser executado
def algoritimos(lista_das_listas, arquivo_num):
    while True:
        print(f"\n--- Definir Algoritimo ---"
              f"\n"
              f"1- Bubble Sort\n"
              f"2- Selection Sort\n"
              f"3- Insertion Sort\n"
              f"4- Merge Sort\n"
              f"5- Rodar Todos\n"
              f"6- Sair")
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

                arquivo_num_org = f"./{arquivo_num}_organizado.txt"
                with open(arquivo_num_org, "w") as arquivo:
                    for i in range(len(lista)):
                        numero = lista[i]
                        if i < (len(lista) - 1):
                            arquivo.write(f"{numero},")
                        else:
                            arquivo.write(f"{numero}")
                
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

                arquivo_num_org = f"./{arquivo_num}_organizado.txt"
                with open(arquivo_num_org, "w") as arquivo:
                    for i in range(len(lista)):
                        numero = lista[i]
                        if i < (len(lista) - 1):
                            arquivo.write(f"{numero},")
                        else:
                            arquivo.write(f"{numero}")

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

                arquivo_num_org = f"./{arquivo_num}_organizado.txt"
                with open(arquivo_num_org, "w") as arquivo:
                    for i in range(len(lista)):
                        numero = lista[i]
                        if i < (len(lista) - 1):
                            arquivo.write(f"{numero},")
                        else:
                            arquivo.write(f"{numero}")

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

                arquivo_num_org = f"./{arquivo_num}_organizado.txt"
                with open(arquivo_num_org, "w") as arquivo:
                    for i in range(len(lista)):
                        numero = lista[i]
                        if i < (len(lista) - 1):
                            arquivo.write(f"{numero},")
                        else:
                            arquivo.write(f"{numero}")

                print(f"\nLista ordenada: {lista}")
                tempo = fim - inicio
                print(f'\nTempo para realizar: {tempo :.3f}')
                salvar_times(lista_das_listas, escolha, tempo)
                return
            case 5:
                print(f"\n--- Rodar Todos Algoritimos")


                print(f"\n--- Bubble Sort")
                escolha_1 = 1
                with open(arquivo_num, "r") as arquivo:
                    conteudo = arquivo.read()
                lista = [int(num.strip()) for num in conteudo.split(",")]
                print(f"\nLista original: {lista}")
                inicio_1 = time.time()
                bubble_sort(lista)
                fim_1 = time.time()
                arquivo_num_org = f"./{arquivo_num}_organizado.txt"
                with open(arquivo_num_org, "w") as arquivo:
                    for i in range(len(lista)):
                        numero = lista[i]
                        if i < (len(lista) - 1):
                            arquivo.write(f"{numero},")
                        else:
                            arquivo.write(f"{numero}")
                print(f"\nLista ordenada: {lista}")
                tempo_1 = fim_1 - inicio_1
                print(f'\nTempo para realizar: {tempo_1 :.3f}')
                salvar_times(lista_das_listas, escolha_1, tempo_1)


                print(f"\n--- Selection Sort")
                escolha_2 = 2
                with open(arquivo_num, "r") as arquivo:
                    conteudo = arquivo.read()
                lista = [int(num.strip()) for num in conteudo.split(",")]
                print(f"\nLista original: {lista}")
                inicio_2 = time.time()
                selection_sort(lista)
                fim_2 = time.time()
                arquivo_num_org = f"./{arquivo_num}_organizado.txt"
                with open(arquivo_num_org, "w") as arquivo:
                    for i in range(len(lista)):
                        numero = lista[i]
                        if i < (len(lista) - 1):
                            arquivo.write(f"{numero},")
                        else:
                            arquivo.write(f"{numero}")
                print(f"\nLista ordenada: {lista}")
                tempo_2 = fim_2 - inicio_2
                print(f'\nTempo para realizar: {tempo_2 :.3f}')
                salvar_times(lista_das_listas, escolha_2, tempo_2)


                print(f"\n--- Insertion Sort")
                escolha_3 = 3
                with open(arquivo_num, "r") as arquivo:
                    conteudo = arquivo.read()
                lista = [int(num.strip()) for num in conteudo.split(",")]
                print(f"\nLista original: {lista}")
                inicio_3 = time.time()
                insertion_sort(lista)
                fim_3 = time.time()
                arquivo_num_org = f"./{arquivo_num}_organizado.txt"
                with open(arquivo_num_org, "w") as arquivo:
                    for i in range(len(lista)):
                        numero = lista[i]
                        if i < (len(lista) - 1):
                            arquivo.write(f"{numero},")
                        else:
                            arquivo.write(f"{numero}")
                
                print(f"\nLista ordenada: {lista}")
                tempo_3 = fim_3 - inicio_3
                print(f'\nTempo para realizar: {tempo_3 :.3f}')
                salvar_times(lista_das_listas, escolha_3, tempo_3)


                print(f"\n--- Merge Sort")
                escolha_4 = 4
                with open(arquivo_num, "r") as arquivo:
                    conteudo = arquivo.read()
                lista = [int(num.strip()) for num in conteudo.split(",")]
                print(f"\nLista original: {lista}")
                inicio_4 = time.time()
                merge_sort(lista)
                fim_4 = time.time()
                arquivo_num_org = f"./{arquivo_num}_organizado.txt"
                with open(arquivo_num_org, "w") as arquivo:
                    for i in range(len(lista)):
                        numero = lista[i]
                        if i < (len(lista) - 1):
                            arquivo.write(f"{numero},")
                        else:
                            arquivo.write(f"{numero}")
                
                print(f"\nLista ordenada: {lista}")
                tempo_4 = fim_4 - inicio_4
                print(f'\nTempo para realizar: {tempo_4 :.3f}')
                salvar_times(lista_das_listas, escolha_4, tempo_4)


                print(f"\n--- Todos algoritimos executados com sucesso")
                escolha_nova_lista = input("Deseja criar uma nova lista (S - N): ")
                if escolha_nova_lista in ["s", "S", "SIM", "Sim", "sim"]:
                       print(f"\n--- Criando uma nova lista")
                       criar_lista(arquivo_num, lista_das_listas) 
                return
            case 6:
                print(f"\n--- Saindo dos Algoritimos")
                return False

#Função que gera o grafico das listas
def gerar_grafico(lista_das_listas):
    # Extrai os dados das listas
    tamanhos = [int(t) for t in lista_das_listas["lista_tamanho"]]
    tempos_bubble = lista_das_listas["lista_temp_bubble"]
    tempos_selection = lista_das_listas["lista_temp_selection"]
    tempos_insertion = lista_das_listas["lista_temp_insertion"]
    tempos_merge = lista_das_listas["lista_temp_merge"]

    # Verifica se há dados
    if not tamanhos:
        print("\nNenhum dado disponível para gerar o gráfico.")
        return

    # Calcula as médias de tempo para cada algoritmo
    def media(lista):
        return sum(lista) / len(lista) if lista else 0

    # Cria dicionário com médias associadas aos tamanhos
    tamanhos_unicos = sorted(set(tamanhos))
    medias_bubble, medias_selection, medias_insertion, medias_merge = [], [], [], []

    for tamanho in tamanhos_unicos:
        # Índices onde o tamanho corresponde
        indices = [i for i, t in enumerate(tamanhos) if t == tamanho]

        # Calcula médias considerando os índices correspondentes
        medias_bubble.append(media([tempos_bubble[i] for i in indices if i < len(tempos_bubble)]))
        medias_selection.append(media([tempos_selection[i] for i in indices if i < len(tempos_selection)]))
        medias_insertion.append(media([tempos_insertion[i] for i in indices if i < len(tempos_insertion)]))
        medias_merge.append(media([tempos_merge[i] for i in indices if i < len(tempos_merge)]))

    # Criação do gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(tamanhos_unicos, medias_bubble, marker='o', label='Bubble Sort')
    plt.plot(tamanhos_unicos, medias_selection, marker='s', label='Selection Sort')
    plt.plot(tamanhos_unicos, medias_insertion, marker='^', label='Insertion Sort')
    plt.plot(tamanhos_unicos, medias_merge, marker='d', label='Merge Sort')

    # Personalização do gráfico
    plt.title("Tempo Médio de Execução x Tamanho da Lista (N)")
    plt.xlabel("Tamanho da Lista (N)")
    plt.ylabel("Tempo Médio (segundos)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Função princial
def main():
    lista_das_listas = {
        "lista_temp_bubble": [],
        "lista_temp_selection": [],
        "lista_temp_insertion": [],
        "lista_temp_merge": [],
        "lista_tamanho": [],
    }

    print(f"\n--- Bem Vindo Ao Sistema ---\n")
    arquivo_num = arquivo()

    while True:
        print(f"\n--- Menu Do Sistema ---"
              f"\n"
              f"1- Tamanho da Lista\n"
              f"2- Algoritimos de Ordenação\n"
              f"3- Dados Salvos\n"
              f"4- Gerar Gráfico de Comparação\n"
              f"5- Gerar Tabela  de Comparação\n"
              f"6- Sair do Progama")
        opcao_menu = int(input("Escolha uma opção: "))

        match opcao_menu:
            case 1:
                criar_lista(arquivo_num, lista_das_listas)
            case 2:
                algoritimos(lista_das_listas, arquivo_num)
            case 3:
                dados(lista_das_listas)
            case 4:
                gerar_grafico(lista_das_listas)
            case 5:
                gerar_tabela(lista_das_listas)
            case 6:
                print("\nSaindo do sistema... Até logo!")
                return False

#Codigo Principal..
main()