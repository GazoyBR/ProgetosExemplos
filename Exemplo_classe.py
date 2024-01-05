# Define a classe Carro
class Carro:
    # O método especial __init__ é um construtor que é chamado ao criar um novo objeto
    def __init__(self, marca, modelo, ano):
        # Inicializa os atributos da instância (marca, modelo, ano e velocidade)
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    # Define um método chamado acelerar que modifica a velocidade do carro
    def acelerar(self, incremento):
        self.velocidade += incremento
        # Imprime uma mensagem indicando a nova velocidade
        print(f"O carro está agora a {self.velocidade} km/h.")

    # Define um método chamado frear que modifica a velocidade do carro
    def frear(self, decremento):
        # Verifica se a velocidade após a frenagem seria negativa
        if self.velocidade - decremento < 0:
            # Se sim, define a velocidade como 0
            self.velocidade = 0
        else:
            # Caso contrário, decrementa a velocidade
            self.velocidade -= decremento
        # Imprime uma mensagem indicando a nova velocidade
        print(f"O carro está agora a {self.velocidade} km/h.")

# Cria uma instância da classe Carro, passando valores para o construtor
meu_carro = Carro(marca="Toyota", modelo="Corolla", ano=2020)

# Chama o método acelerar da instância meu_carro, passando 30 como incremento
meu_carro.acelerar(30)

# Chama o método frear da instância meu_carro, passando 10 como decremento
meu_carro.frear(10)

