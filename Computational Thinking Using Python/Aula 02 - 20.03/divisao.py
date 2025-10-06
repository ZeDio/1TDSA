print("+-+ Verificar Divisão exata +-+")
print("+-----------------------------+")

#entrada
number1 = float(input("Digite o numero 1: "))
number2 = float(input("Digite o numero 2: "))

#processamento
number = number1/number2

if (number == 0):
    print("Os dois numeros deram uma divisão exata!")
else:
    print("Não da uma divisão exata")