# Altere o programa anterior para mostrar no final a soma dos números.
soma = 0
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

for num in range(num1+1,num2):
  print(num)
  soma = soma + num
print("soma =",soma)