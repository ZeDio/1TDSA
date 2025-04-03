executa = input('Executa: (sim ou não)')
cont= 0

while executa == 'sim':
    cont+=1
    executa = input('Executa novamente: (sim ou não)')

print(f'O bloco while executou {cont} vezes!')