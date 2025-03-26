'''
Fazer um algoritmo que leia os dois lados A e B de um triângulo retângulo e calcula a hipotenusa do triângulo.
Para esse caso, considere que ℎ𝑖𝑝𝑜𝑡𝑒𝑛𝑢𝑠𝑎 = √𝐴
2 + 𝐵
2
. Dica: nesse programa, você deve usar a
função matemática Math.sqrt(). Por exemplo, a raiz de 121 ficaria Math.sqrt(121).
'''

#Entrada
a = float(input("\nDigite o primeiro valor: "))
b = float(input("\nDigite o segundo valor: "))

#Procesamento
resul = ((a**2)+(b**2))**0.5

#Saida
print(f"\nA  hipotenusa do triângulo é: {resul}.")