'''
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele
no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
calcular e imprimir o total a receber no final do mês.
'''

#Entrada
nomeVendedor = (input("\nDigite o seu nome: "))
salarioFixo = float(input("\nDigite seu salario fixo: "))
todalVendasCash = float(input("\nDigite o total de vendas efetuadas nesse mês em dinheiro: "))

#Procesamento
comissao = todalVendasCash*0.15
salarioTotal = comissao+salarioFixo

#Saida
print(f"\nOlá {nomeVendedor}, você recebera R$:{salarioTotal} no final do mês..")