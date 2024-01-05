from random import randint

N = int(input("Digite 1 numero: "))
Total = 0
i = 1

while i <= N:
    x = randint(1,50)
    print("Valor {} gerado = {}".format(i,x))

    Total = Total + x

    i += 1

    print("\n Soma dos valores gerados = {}".format(Total)) 






