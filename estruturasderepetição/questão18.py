# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

n = int(input("digite a quantidade de numeros de um conjunto: "))
soma = 0
maior = 0
menor = 100000000000

for num in range(n):
  numero = int(input("digite um numero: "))
  soma = soma + numero
  if numero > maior:
    maior = numero
  if numero < menor:
    menor = numero

print(soma)
print(maior)
print(menor)