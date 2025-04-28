'''
Crie um progama em Python que leia 4 salarios,
calcule a média salarial e imprima os salarios que estiverem abaixo da media..
'''

#Entradas de dados
salarios=[]
soma = 0
i = 0

while i<4:
    salario = float(input("Salário R$: "))
    soma += salario
    salarios.append(salario)
    i += 1

#Media salario
media = soma/4
print(media)

#Imprimir salários que estão abaixo da media
i = 0
while i<4:
    if(media > salarios[i]):
        print(f'Abaixo da média:{salarios[i]:.2f}')
    i += 1