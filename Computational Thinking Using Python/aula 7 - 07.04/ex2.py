'''
Escreva um progama que receba um crédito e depois o preço de itens comprados por um cliente.
O progama deverá parar de solicitar novos preços quando o crédito disponível for insufuciente para pagar por um item.
Ao final, o programa deve exibir o total da compra e o crédito restante.
'''

total = 0
quero_comprar = True

while quero_comprar:
    preco = float(input("Preço: "))
    total += preco
    opcao = input('Continuar Comprando? (s/n)')
    if opcao != 's':
        quero_comprar = False
print(F"total da compra: R${total:.2f}.")