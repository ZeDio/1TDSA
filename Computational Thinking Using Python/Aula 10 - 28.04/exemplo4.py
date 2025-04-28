'''
Crie um progama em Python que leia 4 salarios,
calcule a média salarial e imprima os salarios que estiverem abaixo da media..
'''

#Entradas de dados
salarios=[]
soma = 0

for i in range(4):
    salario = float(input("Salário R$: "))
    soma += salario
    salarios.append(salario)

#Media salario
media = soma/4
print(media)

#Imprimir salários que estão abaixo da media
for salario in salarios:
    if(media > salario):
        print(f'Abaixo da média:{salario:.2f}')