class LivroOfertas:
    def __init__(self):
        self.ofertas = []

    def inserir_oferta(self, posicao, valor, quantidade):
        nova_oferta = {"posicao": posicao, "acao": 0, "valor": valor, "quantidade": quantidade}
        self.ofertas.append(nova_oferta)
        self.atualizar_livro()

    def modificar_oferta(self, posicao, valor, quantidade):
        oferta_existente = self.encontrar_oferta_por_posicao(posicao)
        if oferta_existente:
            oferta_existente["acao"] = 1
            oferta_existente["valor"] = valor
            oferta_existente["quantidade"] = quantidade
            self.atualizar_livro()

    def deletar_oferta(self, posicao):
        oferta_existente = self.encontrar_oferta_por_posicao(posicao)
        if oferta_existente:
            oferta_existente["acao"] = 2
            self.atualizar_livro()

    def encontrar_oferta_por_posicao(self, posicao):
        for oferta in self.ofertas:
            if oferta["posicao"] == posicao:
                return oferta
        return None

    def atualizar_livro(self):
        # Lógica para ordenar e atualizar o livro de ofertas
        self.ofertas = sorted(self.ofertas, key=lambda x: x["valor"])
        # Lógica adicional para atualizar a representação do livro na corretora, enviar mensagens, etc.
        self.notificar_corretora()

    def notificar_corretora(self):
        # Lógica para notificar a corretora sobre as alterações no livro de ofertas
        # Pode incluir envio de mensagens, atualização de dados, etc.
        print("Livro de ofertas atualizado:", self.ofertas)

# Exemplo de Uso:
livro = LivroOfertas()
livro.inserir_oferta(1, 10.0, 5)
livro.inserir_oferta(2, 11.0, 8)
livro.modificar_oferta(1, 9.5, 3)
livro.deletar_oferta(2)
