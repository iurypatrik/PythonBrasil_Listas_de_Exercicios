# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos 
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

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
print("-="*15)
print(f"Bolsonaro obteve {len(bolsonaro)} votos, representando {((len(bolsonaro)/eleitores)*100):.2f}% dos votos.")
print(f"Lula obteve {len(lula)} votos, representando {((len(lula)/eleitores)*100):.2f}% dos votos.")
print(f"Ciro obteve {len(ciro)} votos, representando {((len(ciro)/eleitores)*100):.2f}% dos votos.")
print(f"Brancos/Nulos obteve {len(nulo)} votos, representando {((len(nulo)/eleitores)*100):.2f}% dos votos.")
print("-="*15)