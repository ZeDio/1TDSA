nome = input("Digite o nome do Atleta: ")
saltos = []
soma = 0
maior = 0
i = 0

while i<5:
    salto = float(input(f"Digite a {i+1}° salto: "))
    saltos.append(salto)
    soma += salto
    i+=1

media = soma/5

if(saltos[0] > saltos[1] and saltos[0] > saltos[2] and saltos[0] > saltos[3] and saltos[0] > saltos[4]):
    maior = saltos[0]
if(saltos[1] > saltos[0] and saltos[1] > saltos[2] and saltos[1] > saltos[3] and saltos[1] > saltos[4]):
    maior = saltos[1]
if(saltos[2] > saltos[0] and saltos[2] > saltos[1] and saltos[2] > saltos[3] and saltos[2] > saltos[4]):
    maior = saltos[2]
if(saltos[3] > saltos[0] and saltos[3] > saltos[1] and saltos[3] > saltos[2] and saltos[3] > saltos[4]):
    maior = saltos[3]
if(saltos[4] > saltos[0] and saltos[4] > saltos[1] and saltos[4] > saltos[2] and saltos[4] > saltos[3]):
    maior = saltos[4]

print("\n------------------------\n")
print("Resultado..\n")
print(f"Nome do atleta: {nome}")
print(f"Saltos: {saltos[0]}m - {saltos[1]}m - {saltos[2]}m - {saltos[3]}m - {saltos[4]}m")
print(f"Maior salto: {maior}m")
print(f"Média dos saltos: {media}m")
print("\n------------------------\n")