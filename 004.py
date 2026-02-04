'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
1 - O nome com todas as letras maiúsculas
2 - O nome com todas minúsculas
3 - Quantas letras ao todo (sem considerar os espaços)
4 - Quantas letras tem o primeiro nome
'''

name = input("Nome: ").strip()
list_name = name.split(" ",1)

print(f"Nome Minúsculo: {name.lower()}\n"
      f"Nome Maiúsculo: {name.upper()}\n"
      f"Quantidade de letras sem espaço: {len(name) - name.count(' ')}\n"
      f"Quantidade de letras do primeiro nome: {len(list_name[0])}\n")