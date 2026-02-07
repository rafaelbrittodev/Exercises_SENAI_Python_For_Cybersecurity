'''
Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos
'''

def calc_peso():
    maior_peso = 0
    menor_peso = 0

    for i in range(1,8):
        n = float(input(f"Digite o peso da pessoa {i}: "))
        if maior_peso == 0 and menor_peso == 0:
            maior_peso = n
            menor_peso = n
        elif n > maior_peso:
            maior_peso = n
        elif n < menor_peso:
            menor_peso = n
        else:
            print('Error.')
            break

    print(f'\nO maior peso é: {maior_peso:.2f}\n'
          f'O menor peso é: {menor_peso:.2f}')

calc_peso()

