class Lampada:
    def __init__(self, marca):
        self.marca = marca

    def acender(self):
        print(f"Lâmpada {self.marca} acendendo...")


class LampadaIncandescente(Lampada):
    def __init__(self, marca="Taschibra"):
        super().__init__(marca)

    def acender(self):
        # Ajustado para usar ":" e "amarelada" conforme o enunciado
        print(f"{self.marca}: Luz quente e amarelada acesa.")


class LampadaFluorescente(Lampada):
    def __init__(self, marca="Philips"):
        super().__init__(marca)

    def acender(self):
        # Ajustado para usar ":" e o ponto final
        print(f"{self.marca}: Luz branca fria acesa.")


class LampadaLED(Lampada):
    def __init__(self, marca="Elgin"):
        super().__init__(marca)

    def acender(self):
        # Ajustado para usar ":"
        print(f"{self.marca}: Luz LED de baixo consumo acesa.")



def ligar_lampadas(lista):
    for lampada in lista:
        lampada.acender()



lista_de_lampadas = [
    LampadaIncandescente("Taschibra"),
    LampadaFluorescente("Philips"),
    LampadaLED("Elgin")
]


ligar_lampadas(lista_de_lampadas)