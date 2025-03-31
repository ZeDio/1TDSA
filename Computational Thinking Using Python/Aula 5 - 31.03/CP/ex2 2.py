#Entrada
print("-------------------------------------")
print("Progama Para Calcular IR")

nome = input("\nDigite seu nome: ")
salario = float(input("Digite seu salario: "))
print("-------------------------------------")

#Processamento e Saida
if( 1903.98 >= salario):
    print(f"\n Olá {nome}, você está isento ao imposto de renda(IR), você ira receber {salario}")
    print("\n-------------------------------------")
elif( 1903.98 <= salario and 2826.65 >= salario ):
    ir = salario*0.075
    salarioLiquido = salario-ir
    print(f"\n Olá {nome}, seu salario bruto é de R$:{salario}, você tera que pagar R$:{ir}, e ira receber R$:{salarioLiquido}.")
    print("\n-------------------------------------")
elif( 2826.66 <= salario and 3751.05 >= salario ):
    ir = salario*0.15
    salarioLiquido = salario-ir
    print(f"\n Olá {nome},seu salario bruto é de R$:{salario}, você tera que pagar R$:{ir}, e ira receber R$:{salarioLiquido}.")
    print("\n-------------------------------------")
elif( 3751.06 <= salario and 4664.68 >= salario ):
    ir = salario*0.225
    salarioLiquido = salario-ir
    print(f"\n Olá {nome},seu salario bruto é de R$:{salario}, você tera que pagar R$:{ir}, e ira receber R$:{salarioLiquido}.")
    print("\n-------------------------------------")
elif( 4664.68 <= salario ):
    ir = salario*0.275
    salarioLiquido = salario-ir
    print(f"\n Olá {nome},seu salario bruto é de R$:{salario}, você tera que pagar R$:{ir}, e ira receber R$:{salarioLiquido}.")
    print("\n-------------------------------------")
else:
    print(f"\n Olá {nome}, impossivel calcular")