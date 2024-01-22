Soma = 0
Qtde = 0
X = 1

while X != 0:
    X = int(input("Digite X: "))
    
    if X != 0:  
        Soma = Soma + X 
        Qtde = Qtde + 1  

print("Total dos valores digitados = %d" % Soma)
print("Quantidades de valores = %d" % Qtde)
