# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("\033[mDigite sua nota\033[33m(de 0 a 10):\033[m "))

while True:
  if(nota >= 0 and nota <= 10):
    print("\033[32mValor Válido! Obrigado por usar o nosso programa.")
    break
  else:
    print("\033[31mValor Invalido! Tente Novamente...")
    nota = float(input("\033[mDigite sua nota\033[33m(de 0 a 10): \033[m"))