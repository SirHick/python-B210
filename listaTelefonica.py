agenda = {}

while True:
    print("\n1- Cadastrar")
    print("2 - Consultar")
    print("3 - Consultar toda a lista")
    print("4 - Pesquisar por letra")
    print("5 - Pesquisar por número")
    print("6 - Remover contato")
    print("7 - Sair")

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
        letra = input("Digite a letra inicial: ").upper()
        encontrou = False

        for nome, telefone in agenda.items():
            if nome.upper() .startswith(letra):
                print(f"{nome} - {telefone}")
                encontrou = True

        if not encontrou:
            print("Nenhum contato encontrado")

    elif opcao == "5":
        numTelefone = input("Digite o primeiro número desejado: ")
        encontrouNum = False
        for nome, telefone in agenda.items():
            if telefone.startswith(numTelefone):
                print(f"{nome} - {telefone}")
                encontrouNum = True
        if not encontrouNum:
            print("Nenhum número encontrado")

    elif opcao == "6":
        nome = input("Nome para excluir: ")
        if nome in agenda:
            del agenda[nome]
            print("Contato removido")
        else:
            print("Contato nao encontrado")

    elif opcao == "7":
        print("Saindo...")
        break