# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

num = 1
ant = 0
print(ant,num, end=" ")
for nume in range(11):
  soma = num + ant
  print(soma, end=" ")
  ant = num
  num = soma
