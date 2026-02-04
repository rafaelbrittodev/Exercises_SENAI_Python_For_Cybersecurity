'''
Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.
'''

def imprimir():
    print("-"*30)
    n = int(input("Você deseja imprimir a tabuada de: "))
    print("-" * 30)

    for i in range(10):
        print(f"{n} x {i+1} = {n*(i+1)}")

imprimir()