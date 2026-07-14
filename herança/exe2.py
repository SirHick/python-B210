class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def depositar(self, valor):
        self.saldo += valor
        print(self.saldo)


    def exibir_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, taxa_rendimento):
        super().__init__(titular, saldo)
        self.taxa_rendimento = taxa_rendimento

    def render(self):
        self.saldo = self.saldo * (1 + self.taxa_rendimento)
        print(f"R$ {self.saldo}")


class ContaCorrente(Conta):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite


    def depositar(self, valor):
        if valor <= 0:
            print("Inválido")
        else:
            super().depositar(valor)


    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            print("Saque válido")
            print(self.saldo)
        else:
            print("Saque inválido")
            print(self.saldo)


cp1 = ContaPoupanca("Henrique", 10000, 0.001)
cp1.render()

cc1 = ContaCorrente("Lucas", 20000, 120000)
cc1.depositar(10)
cc1.sacar(140000)

