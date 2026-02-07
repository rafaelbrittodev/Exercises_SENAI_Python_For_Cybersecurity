'''
Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.
'''

letra = input("Digite uma letra: ")

letra = letra.lower()

if letra in 'aeiouáéíóúàèìòùâêîôûãõäëïöü':
    print(f"A letra '{letra}' é uma Vogal.")

# 'a' <= letra <= 'z
# Conferência do invervalo alfabético (código numérico geralmente ASCII ou Unicode)
elif len(letra) == 1 and 'a' <= letra <= 'z':
    print(f"A letra '{letra}' é uma Consoante.")

else:
    print("Entrada inválida. Por favor, digite apenas uma letra.")
