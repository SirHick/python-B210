class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base


    def calcular_salario(self):
        return print(self.salario_base)


class Horista(Funcionario):
    def __init__(self, nome, salario_base, horas_trabalhadas, valor_hora):
        super().__init__(nome, salario_base)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return print(self.horas_trabalhadas * self.valor_hora)

class Mensalista(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)


    def calcular_salario(self):
        super().calcular_salario()

h1 = Horista("Henrique", 1000, 44, 10)
h1.calcular_salario()

m1 = Mensalista("Diego", 4000)
m1.calcular_salario()