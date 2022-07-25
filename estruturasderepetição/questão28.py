# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

media = []
cont = 0

cd = int(input("Digite a quantidade de CD's: "))

for t in range(cd):
  valor = float(input("Digite o preço dos CD's: "))
  media.append(valor)
  cont+=1
  if cont == cd:
    break
print("A media de preço dos CD's é R$ {:.2f}".format(sum(media)/len(media)))