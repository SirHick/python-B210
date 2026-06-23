opcao = 0
votos_joao = 0
votos_ana = 0
votos_pedro = 0

while opcao != 4:
    print(" 1 - João")
    print(" 2 - Ana")
    print(" 3 - Pedro")
    print(" 4 - Encerrar")

    opcao = int(input("Escolha um candidato(a) ou encerrar: "))

    if opcao == 1:
        print(f"\nVotou no João.")
        votos_joao += 1
    elif opcao == 2:
        print(f"\nVotou no Ana.")
        votos_ana += 1
    elif opcao == 3:
        print(f"\nVotou no Pedro.")
        votos_pedro += 1
    elif opcao == 4:
        print(f"\nEncerrando")
    else :
        print("\nOpcao inválida!")

total_votos = votos_joao + votos_ana + votos_pedro

maior_voto = max(votos_joao, votos_ana, votos_pedro)
if maior_voto == votos_joao:
    vencedor = "João"
elif maior_voto == votos_ana:
    vencedor = "Ana"
else:
    vencedor = "Pedro"

print("\n--- RESULTADO DA ELEIÇÃO ---")
print(f"João: {votos_joao}")
print(f"Ana: {votos_ana}")
print(f"Pedro: {votos_pedro}")
print(f"Total de votos: {total_votos}")
print(f"Vencedor(a): {vencedor}")