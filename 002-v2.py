'''
Escreva um programa que leia 6 notas diferentes e faça a média do aluno
Saída esperada:
A sua média final é : 5
'''
#V2
numeros = []
for i in range(6):
    numeros.append(float(input("Digite um numero: ")))

print(f"A sua média final é : {sum(numeros)/len(numeros):.2f}")