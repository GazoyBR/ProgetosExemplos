import time
import random

def desarmar_bomba():
    print("Você tem 10 minutos para desarmar a bomba.")
    print("Resolva os desafios para encontrar os códigos de desativação.")

    # Configuração do timer
    tempo_inicial = 600  # 10 minutos em segundos
    tempo_restante = tempo_inicial

    # Gera um código de desativação aleatório
    codigo_desativacao = random.randint(1, 10)

    while tempo_restante > 0:
        print(f"\nTempo restante: {tempo_restante // 60} minutos e {tempo_restante % 60} segundos")

        # Simula um desafio simples
        resposta = input("Resolva o desafio: ").strip()

        # Verifica se a resposta está correta
        if resposta == str(codigo_desativacao):
            print("Desafio resolvido! Bomba desativada. Você é um herói!")
            break
        else:
            print("Resposta incorreta. A bomba continua ativa.")

        # Atualiza o timer
        time.sleep(5)  # Aguarda 5 segundos
        tempo_restante -= 5

    if tempo_restante <= 0:
        print("Tempo esgotado! A bomba explodiu. Game over.")

if __name__ == "__main__":
    desarmar_bomba()
