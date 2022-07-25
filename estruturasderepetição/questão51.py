# Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
# Imprima no final a soma da série.

den = list(range(1,51))
num = list(range(1,101,2))
print("H = ",end="")
cont = H = 0
for h in range(0,50):
  cont+=1
  print(f"{den[h]}/{num[h]}",end=" ")
  if cont == 50:
    break
  print("+", end=" ")
for h in range(0,50):
  H += den[h]/num[h]
print(f" = {H:.2f}")