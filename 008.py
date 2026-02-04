'''
Crie um programa para jogar JOKEMPO, usando a função random.randint
'''
import random

def jogar():
    print("--- BEM-VINDO AO JOKENPÔ ---")
    print("Escolha sua arma:")
    print("[0] PEDRA")
    print("[1] PAPEL")
    print("[2] TESOURA")

    itens = ('Pedra', 'Papel', 'Tesoura')
    jogador = int(input("Qual é a sua jogada? "))

    if jogador < 0 or jogador > 2:
        print("Opção inválida! Tente novamente.")
        return

    computador = random.randint(0, 2)

    print("-" * 30)
    print(f"Você jogou: {itens[jogador]}")
    print(f"Computador jogou: {itens[computador]}")
    print("-" * 30)

# Regras do jogo
    if jogador == computador:
        print("EMPATE!")
    elif (jogador == 0 and computador == 2) or \
            (jogador == 1 and computador == 0) or \
            (jogador == 2 and computador == 1):
        print("VOCÊ VENCEU!")
    else:
        print("VOCÊ PERDEU!")

jogar()

