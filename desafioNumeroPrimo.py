N = int(input("Digite o número: "))

conta = 0
i = 2

while i < N:
    R = N % i
    if R == 0:
        conta += 1
    i += 1

if conta == 0 and N > 1:
    print("{} é primo".format(N))
else:
    print("{} não é primo".format(N))
