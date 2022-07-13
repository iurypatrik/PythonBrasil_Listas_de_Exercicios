# Faça um programa que calcule o mostre a média aritmética de N notas.
num = 0
numero = []

while num >= 0:
  num = float(input("Digite uma nota:"))
  if num < 0:
    break
  numero.append(num)
print(f"A Soma: '{sum(numero)}' / Quantidade de Numeros: '{len(numero)}' é igual a Media: '{sum(numero)/len(numero)}'")