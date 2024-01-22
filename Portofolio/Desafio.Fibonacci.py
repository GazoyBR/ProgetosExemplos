N = 0

while N < 2:
    try:
        N = int(input("Digite o numero: "))
        if N < 2:
            print("número incorreto, deve ser maior que 2")
    except ValueError:
        print("O dado digitado deve ser um número inteiro.")

A = 0
B = 1
print("0, 1, ", end="") 
i = 0

while i < N - 2:
    C = A + B
    print("{}, ".format(C), end="") 
    A = B 
    B = C
    i += 1
