# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.


qtdp = 0
qtd = 0
for num in range(1,11):
  num = int(input("Digite um numero: "))
  if num%2!=0:
    qtd += 1
  else:
    qtdp += 1
    
print("IMPAR",qtdp)
print("PAR",qtd)



  