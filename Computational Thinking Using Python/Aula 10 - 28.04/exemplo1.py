'''
Crie um progama em Python que leia 4 salarios,
calcule a média salarial e imprima os salarios que estiverem abaixo da media..
'''

#Entradas de dados
soma = 0
salario_1 = float(input('Salário R$: '))
soma += salario_1
salario_2 = float(input('Salário R$: '))
soma += salario_2
salario_3 = float(input('Salário R$: '))
soma += salario_3
salario_4 = float(input('Salário R$: '))
soma += salario_4

#Media salario
media = soma/4
print(f'Média salarial:{media:.2f}')

#Imprimir salários que estão abaixo da media
if(media > salario_1):
    print(f'Abaixo da média: {salario_1:.2f}')
if(media > salario_2):
    print(f'Abaixo da média: {salario_2:.2f}')
if(media > salario_3):
    print(f'Abaixo da média: {salario_3:.2f}')
if(media > salario_4):
    print(f'Abaixo da média: {salario_4:.2f}')
