'''
Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos

#1
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
'''
#2
def calc_peso():
    pesos = []
    for i in range(1,8):
        n = float(input(f"Digite o peso da pessoa {i}: "))
        pesos.append(n)

    print(f'\nO maior peso é: {max(pesos)}\n'
          f'O menor peso é: {min(pesos)}')

calc_peso()

