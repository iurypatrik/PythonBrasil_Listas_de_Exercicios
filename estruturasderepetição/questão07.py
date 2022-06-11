# Faça um programa que leia 5 números e informe o maior número
maior = 0

for nume in range(1,6):
  num = float(input("Digite um numero: "))
  if num > maior:
    maior = num
print(maior)