salarios = []
i = 0
soma = 0
while i<4:
    salario = float(input("Digite seu salario:"))
    soma += salario
    salarios.append(salario)
    i += 1
media = soma/4
print(media)
i=0
while i<4:
    print(f"Salario..{i+1} é {salarios[i]}")
    i+=1