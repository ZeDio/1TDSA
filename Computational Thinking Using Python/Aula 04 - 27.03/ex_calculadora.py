'''
Escreva em progama em Python que simule uma calculadora simples, contendo as quatro operações básicas (+, -, *, /  -  Acrecentemais uma operação). O progama deve ter:
- Menu de operações
- Realizar o calculo escolhido (dois números)
- Apresentar o resultado
'''

#Entrada
print("\n-------------------------")
print("Calculadora basica")
print("1 - Mais(+)")
print("2 - Menos(-)")
print("3 - Multiplicação(*)")
print("4 - Divição(/)")
print("5 - Potencia(**)")
print("-------------------------")
operacao = input("\nDigite a operação que desejá realizar: ")

print("\n-------------------------")
num1 = int(input("Escreva o primeiro numero: "))
num2 = int(input("Escreva o segundo numero: "))

#Procesamento e Saida
match operacao:
    case 1| "Mais" | "+":
        print(f"Resultado obetido: {num1 + num2}.")
    case 2| "Menos" | "-":
        print(f"Resultado obetido: {num1 - num2}.")
    case 3| "Multiplicação" | "*":
        print(f"Resultado obetido: {num1 * num2}.")
    case 4| "Divição" | "/":
        print(f"Resultado obetido: {num1 / num2}.")
    case 5| "Potencia" | "**":
        print(f"Resultado obetido: {num1 ** num2}.")