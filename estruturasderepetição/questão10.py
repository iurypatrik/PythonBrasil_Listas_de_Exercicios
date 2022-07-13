# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

for c in range(1):
  if num2 - num1 >= 2:
    for num in range(num1+1,num2):
      print("\033[32m",num,end = " ")
  elif num1 - num2 >= 2:
    for num in range(num2+1,num1):
      print("\033[32m",num,end = " ")
  else:
    print("\n\033[31mErro! Não existe numeros inteiros nesse intervalo.")
    break
  print("\n\033[mSão os numeros que estão entre \033[31m{} \033[me \033[31m{}.".format(num1,num2))