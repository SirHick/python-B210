class Forma:
    def __init__(self, cor):
        self.cor = cor

    def calcular_area(self):
        pass

    def exibir_info(self):
        print(f"Cor: {self.cor}")


class Circulo(Forma):
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.raio = raio

    def calcular_area(self):
        return 3.14159 * (self.raio ** 2)

    def exibir_info(self):
        super().exibir_info()
        print(f"Forma: Círculo")
        print(f"Área: {self.calcular_area():.2f}")


class Retangulo(Forma):
    def __init__(self, cor, largura, altura):
        super().__init__(cor)
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def exibir_info(self):
        super().exibir_info()
        print(f"Forma: Retângulo")
        print(f"Área: {self.calcular_area():.2f}")


class Triangulo(Forma):
    def __init__(self, cor, base, altura):
        super().__init__(cor)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def exibir_info(self):
        super().exibir_info()
        print(f"Forma: Triângulo")
        print(f"Área: {self.calcular_area():.2f}")



C1 = Circulo("Vermelho", 5)
R1 = Retangulo("Azul", 4, 6)
T1 = Triangulo("Amarelo", 8, 5)

C1.exibir_info()

R1.exibir_info()

T1.exibir_info()