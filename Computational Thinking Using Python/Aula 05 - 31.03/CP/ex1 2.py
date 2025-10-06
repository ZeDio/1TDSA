#Entrada
print("-------------------------------------")
print("Progama Para Calcular Salario")

nomeFuncionario = input("\nDigite seu nome: ")
salarioFixo = float(input("Digite seu salario fixo: "))
vendasSeQ = float(input("Digite o quanto você vendeu durante Segunda e Quarta: "))
vendasQeS = float(input("Digite o quanto você vendeu durante Quinta e Sexta: "))
vendasSeD = float(input("Digite o quanto você vendeu durante Sabado e Domingo: "))
print("-------------------------------------")

#Processamento
comissaoSeQ = vendasSeQ*0.2
comissaoQeS = vendasQeS*0.15
comissaoSeD = vendasSeD*0.1

salarioTotal = salarioFixo + ((comissaoSeQ + comissaoQeS + comissaoSeD)*4)

#Saida
print(f"\nSeu salario total vai ser de R$: {salarioTotal}")
print("\n-------------------------------------")