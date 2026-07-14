class Transporte:
    def __init__(self, nome):
        self.nome = nome


    def viajar(self):
        print("Viajando...")


class Aviao(Transporte):
    def __init__(self):
        super().__init__("Monomotor")

    def viajar(self):
        print("viajando no ar")

class Navio(Transporte):
    def __init__(self):
        super().__init__("Cruzeiro")

    def viajar(self):
        print("viajando na água")

class Trem(Transporte):
    def __init__(self):
        super().__init__("Maria Fumaça")

    def viajar(self):
        print("viajando em terra")


def iniciar_viagem(transporte):
    print(f"{transporte.nome}: ")
    transporte.viajar()

transportes = [Aviao(), Navio(), Trem()]

for forma in transportes:
    iniciar_viagem(forma)