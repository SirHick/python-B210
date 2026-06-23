import random


numero_secreto = random.randint(0, 100)
tentativas = 5

print("Tente adivinhar o número que o programa escolheu (entre 0 e 100)!")

while tentativas > 0:

    palpite = int(input("\nDigite seu palpite: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número.")
        break
    elif palpite < numero_secreto:
        print("O número correto é MAIOR.")
    else:
        print("O número correto é MENOR.")

    tentativas -= 1

else:

    print("\nSuas tentativas acabaram.")
    print(f"O número era: {numero_secreto}")