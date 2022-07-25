# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m

# Resultado final:
# Rodrigo Curvêllo: 5.9 m

a = []
s = []
x = []
cont = 0
while True:
  atleta = str(input("Digite o nome do Atleta: "))
  if atleta == "":
    print("Competição Encerrada")
    break
  a.append(atleta)
  for salt in range(5):
    salto = float(input(f"Digite o resultado do salto numero {salt+1}: "))
    s.append(salto)
  print("-="*15)
  print(f"Atleta: {a[cont]}")
  print(f"Primeiro Salto: {s[0]}m")
  print(f"Segundo Salto: {s[1]}m")
  print(f"Terceiro Salto: {s[2]}m")
  print(f"Quarto Salto: {s[3]}m")
  print(f"Quinto Salto: {s[4]}m")
  print("-="*15)
  print(f"Melhor salto: {max(s)}m")
  print(f"Pior salto: {min(s)}m")
  s.sort()
  del s[0]
  del s[-1]
  print(f"Média dos demais saltos: {sum(s)/len(s):.2f}m")
  print("-="*15)
  x.append(sum(s)/len(s))
  cont +=1
  s.clear()
print("-="*15)
print("Resultado final")
print("-="*15)
for c in range(cont):
  print(f"{a[c]}: {x[c]:.2f}m")
print("-="*15)
