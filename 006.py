'''
Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar
'''

n = int(input("Número? "))

if n % 2 == 0:
    print("Par")
elif n % 2 == 1:
    print("Impar")