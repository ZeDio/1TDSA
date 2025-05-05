for i in range(10):
    print(i)

for letra in 'letras':
    print(letra)   

'''
imprimir os numeros pares entre 1 e 10
'''

for numero in range(0, 11, 2):
    print(numero)

for i in range(1, 11):
    if i%2 == 0:
        print(f'{i} é par')

inicio = 3
fim = 26
for i in range(inicio, fim):
    if i%2 == 0:
        print(f'{i} é par')

dias = ("domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sabado")
print(type(dias))

for dia in dias:
    print(dia)