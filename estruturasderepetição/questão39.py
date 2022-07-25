# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

n = []
a = []

while True:
  nome = input("Digite seu nome: ")
  if nome == "pare":
    break
  altura = int(input("Digite seu altura(cm): "))
  
  n.append(nome)
  a.append(altura)


print(f'\nAluno mais Alto \nNumero: {a.index(max(a))+1}\nNome: {n[a.index(max(a))]}\nAltura: {max(a)}cm')

print(f'\nAluno mais Baixo \nNumero: {a.index(min(a))+1}\nNome: {n[a.index(min(a))]}\nAltura: {min(a)}cm')
