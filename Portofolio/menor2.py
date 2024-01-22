
lista1 = [120, 200, 23, 12, 90, 25, 37, 35, 551, 45]
lista2 = [260, 600, 100, 150, 180, 285, 327, 389, 42, 50]


menor = float('inf')


for n1 in lista1:
  
    for n2 in lista2:
       
        distancia = abs(n1 - n2)
        
    
        if distancia < menor:
            menor = distancia


print(f"A menor distância entre as Listas é: {menor}")
