print("*---------------------*")
print("*- Horas Trabalhadas -*")

#Entrada
salario = float(input("Digite o seu salario: "))
horas = float(input("Digite quantas horas por dia: "))
dias = float(input("DIgite quantos dias por semana: "))

#Processamento
resultado = salario/(horas*dias)*4

#Saida
print(resultado)
