'''
Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos
'''

def leitura():
    maior_peso = 0
    menor_peso = 0
    for i in range(1,8):
        float(input(f"Digite o peso da pessoa {i}: "))

        if maior_peso < i:
            maior_peso = i



leitura()