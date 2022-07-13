# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

n = int(input("digite a quantidade de numeros de um conjunto: "))
soma = 0
maior = 0
menor = 100000000000

for num in range(n):
  numero = int(input("digite um numero: "))
  if numero >= 0 and numero <= 1000:
    soma = soma + numero
    if numero > maior:
      maior = numero
    if numero < menor:
      menor = numero
  else:
    break

print(soma)
print(maior)
print(menor)