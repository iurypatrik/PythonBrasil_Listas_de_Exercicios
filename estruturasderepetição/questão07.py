# Faça um programa que leia 5 números e informe o maior número

#_______________________________
# maior = 0

# for nume in range(5):
#   num = float(input("Digite um numero: "))
#   if num > maior:
#     maior = num
# print("Maior: \033[32m{:.0f}".format(maior))
#__________________________________

num = 0
numero = []

for nume in range(5):
  num = float(input("Digite um número:"))
  numero.append(num)
  numero.sort()
print(f"Maior: \033[32m{max(numero)}")