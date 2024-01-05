A = int(input("Digite um valor para A: "))
B = int(input("Digite um valor para B: "))
C = int(input("Digite um valor para C: "))

if A <= B and A <= C:  # A é o menor dos três
    if B <= C:  # Decide quem é o menor entre B e C
        print("Ordem crescente: {}, {}, {}".format(A, B, C))
    else:
        print("Ordem crescente: {}, {}, {}".format(A, C, B))
elif B <= A and B <= C:  # B é o menor dos três
    if A <= C:  # Decide quem é o menor entre A e C
        print("Ordem crescente: {}, {}, {}".format(B, A, C))
    else:
        print("Ordem crescente: {}, {}, {}".format(B, C, A))
else:  # C é o menor dos três (opção que sobrou, por isso else)
    if A <= B:  # Decide quem é o menor entre A e B
        print("Ordem crescente: {}, {}, {}".format(C, A, B))
    else:
        print("Ordem crescente: {}, {}, {}".format(C, B, A))
