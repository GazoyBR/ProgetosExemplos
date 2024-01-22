lista1 = [120, 200, 23, 12, 90, 25, 37, 35, 551, 45]
lista2 = [260, 600, 100, 150, 180, 285, 327, 389, 2, 50]

num_menor2 = lista2[0]
num_menor1 = lista1[0]

for numero1 in lista1:
    if numero1 < num_menor1:
        num_menor1 = numero1

for numero2 in lista2:
    if numero2 < num_menor2:
        num_menor2 = numero2

menorDistancia = num_menor1 - num_menor2

print("A menor distância é ", menorDistancia)