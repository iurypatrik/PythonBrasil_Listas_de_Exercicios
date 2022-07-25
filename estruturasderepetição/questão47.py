# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7

# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04

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
  for salt in range(7):
    salto = float(input(f"Digite o resultado do salto numero {salt+1}: "))
    s.append(salto)
  print("-="*15)
  print(f"Atleta: {a[cont]}")
  print(f"Primeiro Salto: {s[0]}m")
  print(f"Segundo Salto: {s[1]}m")
  print(f"Terceiro Salto: {s[2]}m")
  print(f"Quarto Salto: {s[3]}m")
  print(f"Quinto Salto: {s[4]}m")
  print(f"Sexto Salto: {s[5]}m")
  print(f"Setimo Salto: {s[6]}m")
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