# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

inter1 = list(range(0,26,1))
inter2 = list(range(26,51,1))
inter3 = list(range(51,76,1))
inter4 = list(range(76,101,1))
i1 = []
i2 = []
i3 = []
i4 = []

while True:
  x = int(input("Digite um numero inteiro, positivo (entre 0 e 100): "))
  if x in inter1:
    i1.append(x)
  if x in inter2:
    i2.append(x)
  if x in inter3:
    i3.append(x)
  if x in inter4:
    i4.append(x)
  if x < 0:
    print("Contagem Encerrada!")
    break

print(f"Entre 0 e 25 temos: {len(i1)} numeros, respectivamente {i1}")
print(f"Entre 26 e 50 temos: {len(i2)} numeros, respectivamente {i2}")
print(f"Entre 51 e 75 temos: {len(i3)} numeros, respectivamente {i3}")
print(f"Entre 76 e 100 temos: {len(i4)} numeros, respectivamente {i4}")
  