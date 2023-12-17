class Item :
    def __init__(self, nome, valor, quantidade) :
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade


class Produto:
    def __init__(self, item1, item2, item3):
        self.itens = [item1, item2, item3]


    def calculaItem(self):
            itentotal = None
            for item in self.itens:
                itentotal += item.valor * item.quantidade
                
                return itentotal
            
    def calculoTotal(self): 
         total = None
         for item in self.itens:
              total += item.valor * item.quantidade
        return total 
    