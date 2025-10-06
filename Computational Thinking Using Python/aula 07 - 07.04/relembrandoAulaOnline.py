'''
Escreva um progama que receba um crédito e depois o preço de itens comprados por um cliente.
O progama deverá parar de solicitar novos preços quando o crédito disponível for insufuciente para pagar por um item.
Ao final, o programa deve exibir o total da compra e o crédito restante.
'''

valorCartao = float(input("\nDigite o valor que você tem no cartão: R$"))
valorProduto = float(input("Digite quanto que vai custar o produto: R$"))
iVezesCompradas = 0

while valorCartao >= valorProduto:
    siOUno = input("\n\nDeseja realizar a compra? (S/N)")
    if siOUno == "s":
        valorCartao = valorCartao - valorProduto
        iVezesCompradas += 1
        print("Você realizou uma compra!")
    else:
        print("Credito Insuficiente")
        break

print(F"Seu saldo disponivel ainda é de R${valorCartao}, e você realizou {iVezesCompradas} compras.")



'''
Escreva um progama que receba um crédito e depois o preço de itens comprados por um cliente.
O progama deverá parar de solicitar novos preços quando o crédito disponível for insufuciente para pagar por um item.
Ao final, o programa deve exibir o total da compra e o crédito restante.
'''

credito = float(input("\n\nCrédito: "))
total = 0 # variavel acumuladora
preco = float(input("Preço: "))

while credito >= preco:
    total += preco
    credito -= preco
    print(F'Crédito restante: R${credito:.2f} \n')
    preco = float(input("Preço: "))

print(F'Total da compra: {total:.2f}')
print(F'Crédito restante: R${credito:.2f}')