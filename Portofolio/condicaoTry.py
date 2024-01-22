from math import cos

try:
    A = int(input("Insira valor de A: "))
    B = int(input("Insira valor de B: "))


    R = A / B

    if A < 0:
        C = cos(A)

        print("Resultado: R = %.1f" % R)
    
except ZeroDivisionError:
    print("B não pode ser zero")

except ValueError:
    print("Digite números inteiros para A e B")
    
except:
    print("Erro desconhecido. Não é possível calcular a divisão")
