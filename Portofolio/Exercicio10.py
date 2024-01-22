


class Produto:
    def __init__(self, nome, quantidade, valor_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

    def calcular_faturamento(self):
        return self.quantidade * self.valor_unitario


produto1 = Produto("Boneco Malandrinho", 17, 18.50)
produto2 = Produto("Spinner Pequeno", 36, 12.00)
produto3 = Produto("Cubo Mágico", 7, 5.90)


faturamento_produto1 = produto1.calcular_faturamento()
faturamento_produto2 = produto2.calcular_faturamento()
faturamento_produto3 = produto3.calcular_faturamento()


faturamento_total = faturamento_produto1 + faturamento_produto2 + faturamento_produto3


print("\nFaturamento por produto:")
print(f"{produto1.nome}: R$ {faturamento_produto1:.2f}")
print(f"{produto2.nome}: R$ {faturamento_produto2:.2f}")
print(f"{produto3.nome}: R$ {faturamento_produto3:.2f}")

print("\nFaturamento total: R$ {:.2f}".format(faturamento_total))
