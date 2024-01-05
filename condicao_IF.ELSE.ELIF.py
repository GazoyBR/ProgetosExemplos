PH = float(input("Digite o valor do PH:"))

if PH < 7.0:
    print("Solução ácida")

elif PH == 7.0:
    print("Soliução neutra")

else:
    print("Solução básica")