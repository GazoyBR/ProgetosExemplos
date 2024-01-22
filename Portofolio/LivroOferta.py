def processar_notificacoes(num_notificacoes, notificacoes):
    livro_ofertas = {}

    for _ in range(num_notificacoes):
        posicao, acao, valor, quantidade = map(float, notificacoes[_].split(','))

        if acao == 0:  # Inserir ou modificar
            livro_ofertas[posicao] = (valor, quantidade)
        elif acao == 1:  # Modificar
            livro_ofertas[posicao] = (valor, quantidade)
        elif acao == 2:  # Deletar
            del livro_ofertas[posicao]

    return livro_ofertas

def imprimir_livro_ofertas(livro_ofertas):
    for posicao, (valor, quantidade) in sorted(livro_ofertas.items()):
        print(f"{int(posicao)},{valor},{int(quantidade)}")

# Exemplo de uso
num_notificacoes = int(input())
notificacoes = []

for _ in range(num_notificacoes):
    notificacoes.append(input())

livro_resultado = processar_notificacoes(num_notificacoes, notificacoes)
imprimir_livro_ofertas(livro_resultado)
