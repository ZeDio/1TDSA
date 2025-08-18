'''
Tentando acessar lista
'''
"""
lista = [1,2,3]
for i in lista:
    print(f'i: {i}')
print(list[3])
"""
lista = [1,2,3]

try:
    print(lista[3])
except IndexError:
    print("erro: o indice da lista está fora da faixa!")
except Exception as e:
    print(f"erro generico: {e}")