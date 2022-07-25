# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

cont = []
while True:
  temp = float(input("Digite uma temperatura: "))
  if temp == 0:
    break
  cont.append(temp)
print(f'Maior:{max(cont)}')
print(f'Menor:{min(cont)}')
print(f'Media:{sum(cont)/len(cont)}')