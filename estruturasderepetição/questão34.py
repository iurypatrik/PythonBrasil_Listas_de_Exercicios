# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input("Digite um numero: "))
tot = 0
for c in range (1, num + 1):
  if num % c == 0:
    tot += 1
if tot == 2:
  print("\n \033[m É um número \033[31mPRIMO")
else:
  print("\n \033[31mNÃO \033[mé um número \033[31mPRIMO")