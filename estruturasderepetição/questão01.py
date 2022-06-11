# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("Digite sua nota(de 0 a 10): "))

while True:
  if(nota >= 0 and nota <= 10):
    print("Valor valido")
    break
  else:
    print("Nota Invalida")
    nota = float(input("Digite sua nota(de 0 a 10): "))