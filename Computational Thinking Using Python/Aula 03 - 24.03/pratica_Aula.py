#comentario de uma linha
'''
comentario de varias linhas - 

if else
Escreva um progama em Python que leia o nome de um aluno e as 3 notas obtidas em um diciplina.
O progama deve calcular a média das 3 notas e definir antes do conceito o status (aprovado - ( >=6 ) ou reprovado).
Alem disso o progama deve definir o conceito de acordo com a média: 

match_case
- conceito A (média >= 9 e media <=10)
- conceito B (média >= 8 e media <9)
- conceito C (média >= 7 e media <8)
- conceito D (média >= 6 e media <7)
- conceito E (média < 6)

'''

#Entrada
nome = input('\nDigite seu nome: ')
n1 = float(input("\nDigite o valor da primeira nota: "))
n2 = float(input("Digite o valor da seguda nota: "))
n3 = float(input("Digite o valor da terceira nota: "))

#Procesamento
media = (n1+n2+n3)/3

if (media >= 9 and media <=10):
    conceito = "A"
elif (media >= 8 and media <9):
    conceito = "B"
elif (media >= 7 and media <8):
    conceito = "C"
elif (media >= 6 and media <7):
    conceito = "D"
else:
    conceito = "E"

#saida
match conceito:
    case "A":
        print(f"\n{nome}, você foi aprovado com o conceito A, com a media: {media:2.1f}")
    case "B":
        print(f"\n{nome}, você foi aprovado com o conceito B, com a media: {media:2.1f}")
    case "C":
        print(f"\n{nome}, você foi aprovado com o conceito C, com a media: {media:2.1f}")
    case "D":
        print(f"\n{nome}, você foi aprovado com o conceito D, com a media: {media:2.1f}")
    case _:
        print(f"\n{nome}, você foi reprovado com o conceito E, com a media: {media:2.1f}")