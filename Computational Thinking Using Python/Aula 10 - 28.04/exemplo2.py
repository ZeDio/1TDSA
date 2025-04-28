'''
Crie um progama em Python que leia 4 salarios,
calcule a média salarial e imprima os salarios que estiverem abaixo da media..
'''

#Entradas de dados
soma = 0
salarios=[0, 0, 0, 0]
salarios[0] = float(input('Salário R$: '))
soma += salarios[0]
salarios[1] = float(input('Salário R$: '))
soma += salarios[1]
salarios[2] = float(input('Salário R$: '))
soma += salarios[2]
salarios[3] = float(input('Salário R$: '))
soma += salarios[3]

#Media salario
media = soma/4
print(f'Média salarial:{media:.2f}')

#Imprimir salários que estão abaixo da media
if(media > salarios[0]):
    print(f'Abaixo da média: {salarios[0]:.2f}')
if(media > salarios[1]):
    print(f'Abaixo da média: {salarios[1]:.2f}')
if(media > salarios[2]):
    print(f'Abaixo da média: {salarios[2]:.2f}')
if(media > salarios[3]):
    print(f'Abaixo da média: {salarios[3]:.2f}')
