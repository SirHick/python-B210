class Funcionario:
    def __init__(self, nome):
        self.nome = nome


    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome}")


class Recepcionista(Funcionario):
    def __init__(self):
        super().__init__("Suellen")

    def cumprimentar(self):
        print(f"Bem-vindo(a)! Meu nome é {self.nome}, posso ajudar?")


class Gerente(Funcionario):
    def __init__(self):
        super().__init__("Luana")

    def cumprimentar(self):
        print(f"Olá! Sou {self.nome}, gerente desta unidade.")


class Tecnico(Funcionario):
    def __init__(self):
        super().__init__("Cláudio")

    def cumprimentar(self):
        print(f"Oi, sou {self.nome}, do suporte técnico.")

def saudacao(cumprimento):
    print(f'{cumprimento.nome}: ')
    cumprimento.cumprimentar()

cumprimentos = [Recepcionista(), Gerente(), Tecnico()]

for cumprimento in cumprimentos:
    saudacao(cumprimento)