class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = None
        self.set_nota(nota)

        #Getter
    def get_nota(self):
            return self.__nota

    #SETTER
    def set_nota(self, nova_nota):
        if 0 < nova_nota <= 10:
            self.__nota = nova_nota
        else:
            print("Nota inválida: Deve ser entre 0 e 10")

    def situacao(self):
        if self.__nota >= 6:
            return "Aprovado(a)"
        elif self.__nota >= 4:
            return "Recuperação"
        else:
            return "Reprovado(a)"

    def exibir_info(self):
        print("="* 30)
        print(f"Aluno: {self.nome}")
        print(f"Nota: {self.get_nota()}")
        print(f"Situação: {self.situacao()}")
        print(f"="* 30)


a1 = Aluno("José", 9.5)
a1.exibir_info()


a2 = Aluno("Joao", 8.0)
a2.exibir_info()

a3 = Aluno("Violeta", 3)
a3.exibir_info()
a3.set_nota(7)
a3.exibir_info()