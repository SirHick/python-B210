class Produto:
    total_cadastrado = 0

    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

        Produto.total_cadastrado += 1

    def valor_em_estoque(self):
        return self.preco * self.qtd

    def aplicar_desconto(self, percentual):
        if 0 < percentual < 100:
            self.preco -= self.preco * (percentual / 100)
        else:
            print("Percentual de desconto inválido")

    def info(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: {self.preco:.2f}")
        print(f"Quantidade: {self.qtd}")
        print(f"Total: {self.valor_em_estoque():.2f}")

    @classmethod
    def exibir_cadastrado(cls):
        print(f"Total de produtos cadastrados {cls.total_cadastrado}")

    #uso da classe
p1 = Produto("Notebook", 8000, 20)
p2 = Produto("Mouse", 399.99, 35)

p1.info()

p2.aplicar_desconto(100)
p2.info()