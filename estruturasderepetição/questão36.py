# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7

# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35

num1 = int(input("\n\033[mDigite um numero \033[33m(de 1 a 10): \033[m"))
num2 = int(input("\n\033[mDigite um numero para começar a tabuada \033[33m(de 1 a 10): \033[m"))
num3 = int(input("\n\033[mDigite um numero para encerrar a tabuada \033[33m(de 1 a 10): \033[m"))
flag = 1
tab = 0
for tab in range(num2,num3+1):
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