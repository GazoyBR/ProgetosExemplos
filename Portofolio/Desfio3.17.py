N = 0

while N < 100 or N > 500:
    try:
        S = int(input("Digite N no intervalo [100, 500]: "))
        N = int(S)
    except:
        print("{} não é um número.".format(N))
        N = 0
    else:
        if N < 100 or N > 500:
            print("O valor lido {} está fora do intervalo".format(N))
        else:
            print("O valor lido {} está ok.".format(N))
    finally:
        print("\n\n")
