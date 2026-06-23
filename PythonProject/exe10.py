senha = '1234'
login = 'admin'
tentativas = 5

while tentativas > 0:
    loginDigitado = input("Digite o seu login: ")
    senhaDigitada = input("Digite a sua senha: ")

    if senhaDigitada == senha and loginDigitado == login:
        print("\nAcesso permitido.")
        break
    else:
        tentativas -= 1
        print("\nUSUÁRIO OU SENHA INCORRETOS")
        if tentativas > 0:
            print(f"{tentativas} TENTATIVAS RESTANTES\n")
else:
    print("Acesso bloqueado. Excedeu as tentativas.")