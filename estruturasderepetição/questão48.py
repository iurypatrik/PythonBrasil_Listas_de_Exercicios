# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:
#   12376489
#   => 98467321

cont = 0
num = str(input("Digite um numero: "))
for n in range(len(num)):
  cont+=1
for c in range(cont):
  print(cont-c,end="")