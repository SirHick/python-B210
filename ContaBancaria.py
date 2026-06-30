class ContaBancaria:

    def __init__(self, titular, numero, saldo = 0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    #depositar
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso")
        else:
            print("Valor de depósito invalido")
    #sacar
    def sacar(self, valor):
        if valor <= 0:
            print("Saque inválido")
        elif valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print(f"Saque no valor de R${valor:.2f} realizado com sucesso")
    #fazer extrato
    def exibir_extrato(self):
        print("="*20)
        print(f"Conta: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")
        print("="*20)

conta1 = ContaBancaria("Lucas", "001-2", 500.00)

conta1.depositar(500.00)
conta1.sacar(100.00)
conta1.exibir_extrato()

conta2 = ContaBancaria("Ana", "003-5", 1000.00)

conta2.depositar(1000.00)
conta2.sacar(500.00)
conta2.exibir_extrato()