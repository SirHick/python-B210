class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.__senha = senha


    '''
    set_senha(nova_senha) - define a senha somente se ela tiver pelo menos 6
    caracteres (caso contrário, avisa e não altera)
    
    verificar_senha(senha_digitada) - retorna True se a senha estiver
    correta, False caso contrário, sem exibir a senha

    exibir_perfil() - exibe nome, email e "Senha: ******"
    '''
    def set_senha(self, nova_senha):
        if len(nova_senha) < 6:
            print("Aviso: A senha deve ter pelo menos 6 caracteres. Alteração negada.")
        else:
            self.__senha = nova_senha
            print("Senha alterada com sucesso!")

    def verificar_senha(self, senha_digitada):
        if senha_digitada == self.__senha:
            return True
        else:
            return False

    def exibir_perfil(self):
        print(f"="* 30)
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Senha: ******")
        print(f"="* 30)

u1 = Usuario("Henrique", "henrique@email.com", "senai123")
u1.set_senha("senai")
u1.verificar_senha("senai12")
u1.exibir_perfil()