# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

num = 0
numero = []

while num >= 0:
  num = int(input("Digite sua idade:"))
  if num < 0:
    break
  numero.append(num)
media = sum(numero)/len(numero)

if media >=0 and media <=25:
  print(f"Como a média de idade foi {media:.0f}, sua turma é Jovem")
if media >=26 and media <=60:
  print(f"Como a média de idade foi {media:.0f}, sua turma é Adulta")
if media >=60:
  print(f"Como a média de idade foi {media:.0f}, sua turma é Idosa")