class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self):

        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numero_portas):
        super().__init__(marca, modelo, ano)
        self.numero_portas = numero_portas


    def exibir_info(self):
        super().exibir_info()
        print(f"Número de Portas: {self.numero_portas}")


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas


    def exibir_info(self):
        super().exibir_info()
        print(f"Cilindradas: {self.cilindradas}")


c1 = Carro("Hyundai", "Veloster", 2017, 3)
c1.exibir_info()

m1 = Moto("KTM", "Enduro", 2020, 300)
m1.exibir_info()