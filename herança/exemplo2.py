class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print(f"{self.nome} emite um som")

    def mover(self):
        print(f"{self.nome} se move")

    def exibir_info(self):
        print(f"Animal: {self.nome}")
        print(f"Idade: {self.idade}")

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        print(f"{self.nome}  late")

    def mover(self):
        print(f"{self.nome} em 4 patas")

    def exibir_info(self):
        super().exibir_info()
        print(f"Raça: {self.raca}")


class Passaro(Animal):
    def __init__(self, nome, idade, pode_voar):
        super().__init__(nome, idade)
        self.pode_voar = pode_voar

    def emitir_som(self):
        print(f"{self.nome}  pia")

    def mover(self):
        if self.pode_voar:
            print(f"{self.nome} pode voar no céu")
        else:
            print(f"{self.nome} corre no chão")

    def exibir_info(self):
        super().exibir_info()
        print(f"Voa: {'SIM' if self.pode_voar else 'NÃO'}")

#USO

c = Cachorro("Tobi", 2, "Border Collie")
p = Passaro("Canário", 1, True)
p2 = Passaro("Pinguim", 3, False)

c.exibir_info()
c.emitir_som()
c.mover()

p.exibir_info()
p.emitir_som()
p.mover()

p2.exibir_info()
p2.emitir_som()
p2.mover()