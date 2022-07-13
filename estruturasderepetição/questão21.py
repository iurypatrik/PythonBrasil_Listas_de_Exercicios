# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("Digite um numero: "))
tot = 0
for c in range (1, num + 1):
  if num % c == 0:
    tot += 1
if tot == 2:
  print("\n \033[m É um número \033[31mPRIMO")
else:
  print("\n \033[31mNÃO \033[mé um número \033[31mPRIMO")
