'''
Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.
'''

letra = input("Digite uma letra: ")

letra = letra.lower()

if letra in 'aeiou':
    print(f"A letra '{letra}' é uma Vogal.")


