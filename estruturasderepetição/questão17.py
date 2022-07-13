# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

# num = int(input("Digite um numero inteiro: "))

# fat = num - 1
# fixo = num

# for nume in range (1,num):
#   result = fixo * fat
#   fixo = result
#   fat = fat - 1

# print(result)

import math
num = int(input("digite um numero:"))
fat = math.factorial(num)
print("\033[mO resultado de {} Fatorial é \033[32m{:.0f}".format(num,fat))
  
