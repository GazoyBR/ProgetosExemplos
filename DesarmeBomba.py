import random

def Bomba():

print("Bem vindo ao jogo Desarme a bomba !")
print("Neste jogo voce tem 3 cores de fios e terá q corta 1 fio para poder desarma-la, boa sorte !!")

lista = [vermelho, verde, amarelo]
desativa = random.choice(lista)

try:

escolha = int(input("Escolha a cor do fio que quer cortar"))

    if escolha == desativa:
        print("Bomba desativada com sucesso!")

        else:
        print("Voce morreu")

        if __name__ == "__main__":
        bomba() 





