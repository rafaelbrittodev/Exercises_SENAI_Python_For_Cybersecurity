'''
Escreva um programa que calcule a soma dos números de 1 a 100 usando um loop
'''

def soma():
    soma = 0
    for i in range(1,101):
        print(f"{soma} + {i} = {soma+i}")
        soma += i

soma()
