'''
Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.
V = (4/3) . π . r³
A = 4 . π . r²
Saída esperada:
Volume da Esfera: Y
Área da esfera: X
'''

import math

R = float(input("Raio: "))

V = (4/3) * math.pi * R**3
A = 4 ** math.pi * R**2

print(f"Volume da Esfera: {V:.2f}")
print(f"Área da Esfera: {A:.2f}")