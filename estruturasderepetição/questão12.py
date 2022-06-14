# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

num1 = int(input("Digite um numero de 1 a 10: "))
flag = 1
tab = 0
while tab < 11:
  flag += 1
  if (num1 <= 10 and num1 >= 1):
    print("{} X {} = {}" .format(num1,tab,(num1*tab)))
    tab += 1
  else:
    num1 = int(input("Digite um numero de 1 a 10: "))
    if flag > 3:
      break