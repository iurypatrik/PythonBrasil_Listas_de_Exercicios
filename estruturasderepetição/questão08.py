# Faça um programa que leia 5 números e informe a soma e a média dos números.

# ________________________________

# soma = 0

# for nume in range(5):
#   num = float(input("Digite um numero: "))
#   soma += num
#   media = soma/5
# print("\n\033[mA soma desses numeros é igual a \033[32m{:.0f} \033[me a média é igual a \033[32m{:.0f}.".format(soma,media))

# _________________________________

num = 0
numero = []

for nume in range(5):
  num = float(input("Digite um número:"))
  numero.append(num)
  numero.sort()
print(f"Soma: \033[32m{sum(numero)}")
print(f"Media: \033[32m{sum(numero)/5}")