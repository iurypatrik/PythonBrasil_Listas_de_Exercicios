# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

N = int(input("Digite um valor para N: "))

num = list(range(2,N+1))
print("H = 1 + ",end="")
cont = 0
for h in range(N):
  cont+=1
  print(f"1/{num[h]}",end=" ")
  if cont == N-1:
    break
  print("+", end=" ")