class Cofre:
    def __init__(self, valor = 0, dono = ""):
        self.__valor = valor
        self.dono = dono

    def get_dono(self):
        return self.dono

    '''
    depositar(valor) - adiciona ao cofre (somente valores positivos)
    retirar(valor) - remove do cofre(não pode ficar negativo)
    get_valor() - retorna o valor atual(getter)
    exibir_saldo() - exibe dono e saldo atual
    '''

    def depositar(self, deposito):
        if deposito > 0:
            self.__valor += deposito
        else:
            print("Depósito inválido: deve ser maior que zero")

    def retirar(self, saque):
        if saque > self.__valor:
            print("Saque inválido: valor maior do que o em sua conta")
        else:
            self.__valor -= saque


    def get_valor(self):
        return self.__valor

    def exibir_saldo(self):
        print(f"="* 30)
        print(f"Dono: {self.get_dono()}")
        print(f"Saldo: {self.get_valor()}")
        print(f"="* 30)

c1 = Cofre(1000, "Glauco")
c1.depositar(1)
c1.retirar(10)
c1.exibir_saldo()

c2 = Cofre(20000, "Márcia")
c2.depositar(100)
c2.retirar(1000)
c2.exibir_saldo()