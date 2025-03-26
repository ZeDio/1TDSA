'''
Escreva um programa que leia o número de cadastro de um funcionário, seu número de horas trabalhadas,
o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre na tela o número e o
salário do funcionário
'''

#Entrada
numCadastro = float(input("\nDigite teu codigo: "))
numHorasTrabalhadas = float(input("\nDigite as horas trabalhadas: "))
numQueRecebePorHora = float(input("\nDigite quanto você recebe por hora trabalhada: "))

#Procesamento
resul = numHorasTrabalhadas*numQueRecebePorHora

#Saida
print(f"\nQuanto recebe o funcionario: {resul}. \nCodigo do funcionario: `{numCadastro}")