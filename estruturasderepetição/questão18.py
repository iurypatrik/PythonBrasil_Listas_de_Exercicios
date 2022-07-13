# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

n = int(input("digite a quantidade de numeros de um conjunto: "))
soma = maior = menor = 0

for c in range(n):
  numero = int(input("digite um numero: "))
  soma = soma + numero
  if numero > maior:
    maior = numero
  if numero < menor:
    menor = numero
  else:
    maior = menor = numero
    
print("Soma =",soma)
print("Maior =", maior)
print("Menor =", menor)


# N = int(input("Digite N: "))
# i = 0
# ma = 'maior'
# me = 'menor'
# me = x
# while i < N:
#     x = float(input("Digite um número: "))
#     ma = x
#     me < ma
#     i = i + 1
#     if x > ma:
#         ma = x
#     if x < me:
#         me = x
# print ('O maior valor digitado foi {} e o menor foi {}'.format(ma,me))