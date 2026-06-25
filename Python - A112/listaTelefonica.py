agenda = {}

while True:
    print("\n1- Cadastrar")
    print("2 - Consultar")
    print("3 - Consultar toda a lista")
    print("4 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        if nome in agenda:
            print("Nome já cadastrado")
        else:
            while True:
                telefone = input("Telefone: ")
                if telefone != "":
                    break
                print("Telefone obrigatório")
            agenda[nome] = telefone
            print("Contato cadastrado.")
    elif opcao == "2":
        nome = input("Nome para buscar: ")
        if nome in agenda:
            print("Telefone", agenda[nome])
        else:
            print("Contato nao encontrado")
    elif opcao == "3":
        if len(agenda) == 0:
            print("Lista vazia")
        else:
            print("\nContatos Cadastrados")
            cont = 1
            #FOR que percorre 2 argumentos
            for nome, telefone in agenda.items():
                print(f"{cont} - Nome: {nome} - Telefone: {telefone}")
                cont += 1
    elif opcao == "4":
        print("Saindo...")
        break