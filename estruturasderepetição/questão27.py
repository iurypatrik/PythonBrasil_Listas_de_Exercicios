# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
media = []
cont = 0

turma = int(input("Digite a quantidade de turmas: "))

for t in range(turma):
  alunos = int(input("Digite a quantidade alunos por turma: "))
  media.append(alunos)
  cont+=1
  if alunos >40 or cont == turma:
    break
print("A media de Alunos por turma é {:.2f}".format(sum(media)/len(media)))
