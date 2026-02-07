'''
Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci
'''

# 0 1 1 2 3 5 8 13 21 34 55
n = int(input('Digite qual termo de Fibonacci deseja encontrar? '))

i = 0
ant = 0
atual = 0

while i < n:
    if i == 0:
        atual = 0

    if i == 1 or i == 2:
        ant = 0
        atual = 1

    proximo = ant + atual
    ant = atual
    atual = proximo

    i += 1
    print(atual)