'''
Escreva um progama em python que leia 5 nomes, armazenando em uma lista e exiba a quantidade de nomes que iniciam com VOGAL
'''

nomes = []
nomesVogal = []
qtd = 0
for nome in range(5):
    nomes.append(input("Insira o nome: "))
for verificar in nomes:
    if verificar[0].upper() == "A" or verificar[0].upper() == "E" or verificar[0].upper() == "I" or  verificar[0].upper() == "O" or  verificar[0].upper() == "U":
        nomesVogal.append(verificar)
        qtd+=1
print(f"\n{qtd} nomes começam com vogal")
print(nomesVogal)