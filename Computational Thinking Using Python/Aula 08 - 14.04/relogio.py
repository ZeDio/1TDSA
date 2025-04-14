import time

hora = int(input("Digite Hora: "))
minuto = int(input("Digite Minuto: "))
segundo = int(input("Digite segundo: "))

h = 0
while h < 24:
    m = 0
    while m < 60:
        s = 0
        while s < 60:
            print(f"{h}:{m}:{s}")
            time.sleep(1)
            if h== hora and m== minuto and s== segundo:
                print("\nALARME ♥")
                break
            s+=1
        if h== hora and m== minuto:
            break
        m+=1
    if h== hora:
        break
    h+=1