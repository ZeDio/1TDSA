'''
Fazer um algoritmo que leia dois números e imprime a divisão do maior pelo menor.”.
'''

#Entrada
numero1 = int(input("\nDigite o numero 1: "))
numero2 = int(input("\nDigite o numero 2: "))

#Procesamento
if (numero1 >= numero2):
    resulDivisao = numero1/numero2
else:
    resulDivisao = numero2/numero1

#Saida
print(f"A divisão do maior pelo menor: {resulDivisao}")
