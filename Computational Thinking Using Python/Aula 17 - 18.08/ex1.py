'''
Tratamentos de erros (try-except)
'''

while True:
    try:
        num = int(input("numero: "))
        if num < 0:
            print(f'Numero: {num}, agora vai parar sua besta')
            break
        print(f'Numero: {num}')
    except ValueError:
        print('Entrada Invalida, Por Favor digite um numero.')
    