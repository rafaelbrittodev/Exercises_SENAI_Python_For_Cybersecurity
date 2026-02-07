'''
Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até que o usuário acerte o número.
E no final, retorne também a quantidade de tentativas necessárias.
'''
import random

def jogar():
    x = random.randint(1,10)
    i = 1
    n = int(input(f'Digite seu número {i}: '))

    while n != x:
        i += 1
        n = int(input(f'Digite seu número {i}: '))

    print(f'\nParabéns, você acertou! O número é "{x}"!\n'
          f'Você teve {i} tentativas.')

jogar()