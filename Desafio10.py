class BonecoMalandrinho:
    def __init__(self, quantidade):
        self.nome = "Boneco Malandrinho"
        self.valor = 18.50
        self.quantidade = quantidade

    def calcular_total(self):
        return self.valor * float(self.quantidade)


class SpinnerPequeno:
    def __init__(self, quantidade):
        self.nome = "Spinner Pequeno"
        self.valor = 12.00
        self.quantidade = quantidade

    def calcular_total(self):
        return self.valor * float(self.quantidade)


class CuboMagico:
    def __init__(self, quantidade):
        self.nome = "Cubo Mágico"
        self.valor = 5.90
        self.quantidade = quantidade

    def calcular_total(self):
        return self.valor * float(self.quantidade)


def calcular_total_geral(produtos):
    total_geral = 0
    for produto in produtos:
        total_geral += produto.calcular_total()
    return total_geral


boneco = BonecoMalandrinho(input("Informe quantos Bonecos Malandrinho você vendeu: "))
spinner = SpinnerPequeno(input("Informe quantos Spinners Pequenos você vendeu: "))
cubo = CuboMagico(input("Informe quantos Cubos Mágicos você vendeu: "))

produtos = [boneco, spinner, cubo]

total_geral = calcular_total_geral(produtos)

print(f"Total de Boneco Malandrinho: {boneco.calcular_total()}")
print(f"Total de Spinner Pequeno: {spinner.calcular_total()}")
print(f"Total de Cubo Mágico: {cubo.calcular_total()}")
print(f"Total Geral: {total_geral}")
