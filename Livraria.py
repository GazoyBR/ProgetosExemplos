Posicao = 0
Acao = 0
Inserir = 0
Modificar = 1
Deletar = 2
livro = 0

class LivrosOferta:
    def __init__(self, nome, quantidade, valor_unitario):
        self.nome = input()
        self.quantidade = input()
        self.valor_unitario = input()
        self.Posicao = 0

print("informe a opção desejada: ")
Acao = int(input(" [1] Inserir "  " [2] Modificar" " [3] Deletar" ))


if Acao == Inserir :
    print("Informe nome, quantidade e valor do livro")

    livro = LivrosOferta


elif Acao == Modificar :
    print("oque quer modificar ")

elif Acao == Deletar :
    print("Qual livro quer deletar")







