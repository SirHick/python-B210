class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.__estoque = estoque

    '''
    get_estoque() - retorna a quantidade em estoque
    
    adicionar_estoque(quantidade) - aumenta o estoque (somente valores
    positivos)
    
    vender(quantidade) - diminui o estoque se houver quantidade suficiente,
    caso contrário, avisa

    exibir_info() - exibe nome, preço e estoque atual
    '''

    def get_estoque(self):
        return self.__estoque

    def adicionar_estoque(self, qtd):
        if qtd <= 0:
            print("Erro ao adicionar: valor negativo")
        else:
            self.__estoque += qtd

    def vender(self, quantidade):
        if quantidade > self.__estoque:
            print("Erro ao vender: estoque insuficiente")
        else:
            self.__estoque -= quantidade

    def exibir_info(self):
        print("="* 30)
        print(f"Nome: {self.nome}")
        print(f"Preco: {self.preco}")
        print(f"Estoque atual: {self.get_estoque()}")
        print("="* 30)

