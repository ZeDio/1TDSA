#Entrada
a = float(input("\nDigite o primeiro valor: "))
b = float(input("\nDigite o segundo valor: "))
c = float(input("\nDigite o terceiro valor: "))
pi = 3.14159

#Procesamento
exA = (a*c)/2
exB = pi*c**2
exC = (a+b)/2*c
exD = b*b
exE = a*b
exF = 2*(a*b)

#Saida
print(f"\nA área do triângulo retângulo que tem A por base e C por altura é: {exA}.")
print(f"\nA área do círculo de raio C é: {exB}.")
print(f"\nA área do trapézio que tem A e B por bases e C por altura é: {exC}.")
print(f"\nA área do quadrado que tem lado B é: {exD}.")
print(f"\nA área do retângulo que tem lados A e B é: {exE}.")
print(f"\nO perímetro do retângulo que tem lados A e B é: {exF}.")