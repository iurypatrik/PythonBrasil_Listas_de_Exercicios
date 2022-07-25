# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

lista = []
while True:
  num = int(input("Digite um numero: "))
  if num > 2:
    break

for x in range(2,num):
  tot = 0
  for c in range (1, x + 1):
    if x % c == 0:
      tot += 1
  if tot == 2:
    lista.append(x)
print(f"\n\033[35mEntre 1 e {num} temos {lista} que são primos")

tots = 0
for z in (lista):
  print(f"\n\033[34mCONFERINDO O NUMERO {z}")
  tots = 0
  for c in range (1, z + 1):
    if z % c == 0:
      print("\033[31m",end=" ")
      tots += 1
    else:
      print("\033[m",end=" ")
    print("{}".format(c),end=" ")
  print(f"\n \033[mO número {z} foi divisivel \033[31m{tots} Vezes")