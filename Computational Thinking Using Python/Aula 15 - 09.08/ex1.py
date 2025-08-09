'''
Escreva um programa em Python que simule o cálculo de notas de um aluno em diferentes diciplinas. O programa deve modular e utilizar as estruturas de controle e funções

1. Requisitos de programa
- Função calcular_media(notas)
    * deve receber uma lista de notas como parâmetro
    * deve ter uma estrutura de repetição (for ou while) para percorrer as listas e somar as notas
    * deve retornar a média das notas

- Função verificar_aprovacao(media, media_minima)
    * deve recebere a média do aluno e a média minima para aprovação
    * deve usar condicionais para verificar o status do aluno
    * se a média for maior ou igual a média mínima, retornar a string "Aprovado"
    * se a média for maior ou igual a 5.0 e menor que a média mínima, deve retornar a string "Recuperação"
    * caso contrário, deve retornar a string "Reprovado"

- Função Princpal main()
    * lista de disciplinas
    * média mínima de aprovação
    * estrutura de repetição iterar sobre as disciplinas
    * para cada disciplina, o usuário devera inserir três notas
    * chamar a função calcular_media() para obter a média da disciplina 
    * chamar a função verificar_aprovacao() para obter o status 
    * imprimir a média e o status para cada disciplina  
'''

def calcular_media(notas): 
    '''
    Calcula a média de uma lista de notas
    - recebe um lista de notas
    - retorna a média das notas
    '''
    soma = 0
    #percorre a lista e soma todos os elementos da lista
    for nota in notas:
        soma += nota

    # validar a divisão por zero
    if len(notas) > 0:
        return soma / len(notas)
    else:
        return 0 

def verificar_aprovacao(media, media_minima):
    '''
    Verifica o status de aprovação do aluno 
    - recebe a média e a média mínima por parâmetro 
    - retorna o status - aprovado, recuperação ou reprovado  
    '''
    if media >= media_minima:
        return "Aprovado"
    elif media >= 5 and media < media_minima:
        return "Recuperação"
    else:
        return "Reprovado"

def main():
    '''
    Função principal do programa
        * lista de disciplinas
        * média mínima de aprovação
    '''

    #lista de disciplinas 
    disciplinas = ['Python', 'Java', 'Front-end']
    media_aprovacao = 7.0

    print('*-- Sistema de Cálculo de Notas --*')

    #percorre (iterar) a lista de disciplinas
    for disciplina in disciplinas:
        print(f'\nDisciplina: {disciplina}')
        
        # lista de notas da disciplina
        notas = []

        #obter as notas de cada disciplina
        for i in range(3):
            nota = float(input(f'Digite a nota {i+1}: '))
            notas.append(nota)

        #calcula a média e verifica o status
        media_final = calcular_media(notas)
        status = verificar_aprovacao(media_final, media_aprovacao)

        #imprime os resultados
        print(f'Média em {disciplina}: {media_final:.2f}')
        print(f'Status: {status}')

#Programa principal
main()
