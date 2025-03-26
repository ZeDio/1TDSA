'''
Fazer um algoritmo que leia dois números L e R. O programa deve verificar a maior área entre um quadrado
de lado L e um círculo de raio R. Imprimir na tela qual o maior: "Quadrado" ou "Círculo".
'''

#Entrada
numeroL = float(input("\nDigite o numero L: "))
numeroR = float(input("\nDigite o numero R: "))
pi = 3.14

#Procesamento
quadrado = numeroL*numeroL
circulo = pi*(numeroR**2)

#Saida
if (quadrado >= circulo):
    print("O quadrado tem a área maior do que a do círculo")
else:
    print("O círculo tem a área maior do que a do quadrado")