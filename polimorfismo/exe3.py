class Lampada:
    def __init__(self, marca):
        self.marca = marca


    def acender(self):
        print(f"Lâmpada {self.marca} acendendo...")


class LampadaIncandescente(Lampada):
    def __init__(self):
        super().__init__("Taschibra")

    def acender(self):
        print(f"{self.marca} - Luz quente e amarela acesa")

class LampadaFluorescente(Lampada):
    def __init__(self):
        super().__init__("Philips")

    def acender(self):
        print(f"{self.marca} - Luz branca fria acesa")

class LampadaLED(Lampada):
    def __init__(self):
        super().__init__("Elgin")

    def acender(self):
        print(f"{self.marca} - Luz LED de baixo consumo acesa.")

def ligar_lampadas(lista):
