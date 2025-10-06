print("+-------------------------+")
print("+--- Comissão Vendedor ---+")

#entrada
vendedor = input("Digite o seu nome: ")
codigoPeca = input("Digite o codigo da peça: ")
precoPeca = float(input("Digite o preço da peça: "))
quantidadeVendida = float(input("Digite quantas peças vendidas: "))

#processamento
valorTotal = precoPeca*quantidadeVendida
valorComicao = valorTotal*0.05

#saída
print("+-------------------------+")
print("+- Vendedor: -+")
print(vendedor)
print("+- Valor Total De Vendas: -+")
print(valorTotal)
print("+- Comição do Vendedor Total: -+")
print(valorComicao)
