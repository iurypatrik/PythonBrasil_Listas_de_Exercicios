# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

import math
num = int(input("digite um numero:"))
print(f'{num}! = ',num,end="")
for n in range(num-1,0,-1):
  print(f'.{n}',end="")
print(" =",math.factorial(num))
