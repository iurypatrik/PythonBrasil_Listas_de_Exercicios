# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

num1 = int(input("\n\033[mDigite um numero \033[33m(de 1 a 10): \033[m"))
flag = 1
tab = 0
while tab < 11:
  flag += 1
  if (num1 <= 10 and num1 >= 1):
    print("\033[m{} X {} = \033[32m{}" .format(num1,tab,(num1*tab)))
    tab += 1
  else:
    print("\n\033[31mEste numero não esta entre 1 e 10, Tente novamente...")
    num1 = int(input("\n\033[mDigite um numero de 1 a 10: "))
    if flag > 2:
      print("\n\033[31mErro! Numero de tentativas excedido.")
      break