# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

num = 1
import math

while num != -1:
  num = int(input("digite um numero:"))
  if num < 0 or num > 16:
    break
  fat = math.factorial(num)
  print("O resultado de {} Fatorial é {:.1f}".format(num,fat))


    