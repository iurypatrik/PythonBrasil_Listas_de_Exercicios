# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
bolsonaro = []
lula = []
ciro = []
nulo = []

eleitores = int(input("Quantos Eleitores irão votar? "))
print("-="*15)
print("Bolsonaro: 17\nLula: 13\nCiro: 12")
print("-="*15)
for e in range(eleitores):
  voto = int(input("Digite o numero do seu candidato: "))
  if voto == 17:
    bolsonaro.append(1)
  elif voto == 13:
    lula.append(1)
  elif voto == 12:
    ciro.append(1)
  else:
    nulo.append(1)
print(f"\nBolsonaro obteve {len(bolsonaro)} votos.")
print(f"Lula obteve {len(lula)} votos.")
print(f"Ciro obteve {len(ciro)} votos.")
print(f"Brancos/Nulos obteve {len(nulo)} votos.")
  