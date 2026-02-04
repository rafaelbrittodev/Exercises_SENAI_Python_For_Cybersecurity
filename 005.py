'''
Crie um programa que leia uma frase e mostre:
1 - Quantas vezes aparece a letra “a”
2 - Em que posição ela aparece a primeira vez
3 - Em que posição ela aparece na última vez
'''

frase = input("Digite uma frase: ")

print(f"Quantidade de A: {frase.count('a')}")
print(f"Primeira posição de A: {frase.find('a')+1}")
print(f"Última posição de A: {frase.rfind('a')+1}")