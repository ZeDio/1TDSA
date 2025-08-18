'''
divisão por 0
'''

'''
-- Antigo --
num1 = int(input('Numero: '))
num2 = int(input('Numero: '))
result = num1/num2
print(f'Resultado da Divisão é {result}')
'''

continuar = True
while True:
    try:   
        num1 = int(input('Numero: '))
        num2 = int(input('Numero: ')) 
        result = num1/num2
        print(f'Resultado da Divisão é {result}')
    except ZeroDivisionError:
        print('Divisão por zero não pode.')
    except ValueError:
        print('Divisão com letra não funciona.')
    finally:
        teste = int(input('1 - para contunuar?'))
        if teste != 1:
            continuar = False