class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__historico = []

    def get_cpf(self):
        cpf= self.__cpf
        return f"***.***.{cpf[8:11]}-{cpf[11:]}"

    def get_idade(self):
        return self.__idade

    def get_historico(self):
        return self.__historico

    #Setter
    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self.__idade = nova_idade
        else:
            print("Idade inválida")


    #Metodos
    def adicionar_historico(self, diagnostico):
        self.__historico.append(diagnostico)
        print(f"Diagnóstico registrado: {diagnostico}")

    def exibir_prontuario(self):
        print("="* 30)
        print(f"Paciente: {self.nome}")
        print(f"CPF: {self.get_cpf()}")
        print(f"Idade: {self.__idade}anos")
        print(f"Histórico: ")
        if self.__historico:
            for item in self.__historico:
                print(f"-{item}")
        else:
            print("Nenhum diagnóstico encontrado.")
        print("="*30)


p1 = Paciente("Cleber", "12345678922", 40)
p1.adicionar_historico("Gripe")
p1.adicionar_historico("Febre")
p1.set_idade(41)
p1.exibir_prontuario()


p2 = Paciente("Vanessa", "98765432101", 20)
p2.adicionar_historico("Pneumonia")
p2.set_idade(21)
p2.exibir_prontuario()