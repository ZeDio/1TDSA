carros = []
consumos = []
i=0

print("\n------------------------\n")
while i<5:
    print(f"Veiculo {i+1}")
    carro = input("Nome: ")
    mediaKM = float(input("Km por litro: "))
    carros.append(carro)
    consumos.append(mediaKM)
    i+=1

if(consumos[0] > consumos[1] and consumos[0] > consumos[2] and consumos[0] > consumos[3] and consumos[0] > consumos[4]):
    menor = carros[0]
if(consumos[1] > consumos[0] and consumos[1] > consumos[2] and consumos[1] > consumos[3] and consumos[1] > consumos[4]):
    menor = carros[1]
if(consumos[2] > consumos[0] and consumos[2] > consumos[1] and consumos[2] > consumos[3] and consumos[2] > consumos[4]):
    menor = carros[2]
if(consumos[3] > consumos[0] and consumos[3] > consumos[1] and consumos[3] > consumos[2] and consumos[3] > consumos[4]):
    menor = carros[3]
if(consumos[4] > consumos[0] and consumos[4] > consumos[1] and consumos[4] > consumos[2] and consumos[4] > consumos[3]):
    menor = carros[4]
print("\n------------------------\n")

i=0
while i<5:
    litros = 1000/consumos[i]
    preco = litros*6.89
    print(f"{i+1}° - {carros[i]} -- {consumos[i]} - {litros:.2f} - {preco:.2f}")
    i+=1
print(f"O menor consumo e do {menor}")

print("\n------------------------\n")