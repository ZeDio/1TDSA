'''
Fazer um algoritmo que leia três números e imprime o maior deles
'''

#Entrada
numero1 = int(input("\nDigite o numero 1: "))
numero2 = int(input("\nDigite o numero 2: "))
numero3 = int(input("\nDigite o numero 3: "))

#Procesamento e saida
if (numero1 >= numero2 and numero1 >= numero3):
    print(F"\nO numero {numero1} é maior que os {numero2} e {numero3}.")
elif(numero2 >= numero1 and numero2 >= numero3):   
    print(F"\nO numero {numero2} é maior que os {numero1} e {numero3}.")
else:
    print(F"\nO numero {numero3} é maior que os {numero1} e {numero2}.")