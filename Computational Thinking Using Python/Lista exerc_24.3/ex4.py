'''
Fazer um algoritmo que lê dois números inteiros e imprime os números consecutivos desses números. (Por
exemplo: se o usuário digitar 2 e -9, a saída deverá ser 3 e -8, porque 3 é consecutivo de 2. –8 é consecutivo
de –9)
'''

#Entrada
n1 = float(input("\nDigite o primeiro numero: "))
n2 = float(input("\nDigite o segundo numero: "))

#Procesamento
resul1 = n1 + 1
resul2 = n2 + 1

#Saida
print(f"Consecutivo do {n1} é {resul1}")
print(f"\nConsecutivo do {n2} é {resul2}")