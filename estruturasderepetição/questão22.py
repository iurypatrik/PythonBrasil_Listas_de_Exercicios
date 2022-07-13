# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = int(input("Digite um numero: "))
tot = 0
for c in range (1, num + 1):
  if num % c == 0:
    print("\033[31m",end=" ")
    tot += 1
  else:
    print("\033[m",end=" ")
  print("{}".format(c),end=" ")
print("\n \033[m O número {} foi divisivel \033[31m{} Vezes" .format(num,tot))
if tot == 2:
  print("\n \033[m Por isso é um número \033[31mPRIMO")
else:
  print("\n \033[m Por isso \033[31mNão \033[mé um número \033[31mPRIMO")
