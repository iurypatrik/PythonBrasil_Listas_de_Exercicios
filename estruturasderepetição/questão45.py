# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:
# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A

# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

gabarito = ["A","B","C","D","E","E","D","C","B","A"]
resposta = []
alunos = []
cont = []
nota = []
while True:
  aluno = str(input("Digite seu nome:"))
  alunos.append(aluno)
  if aluno == "pare":
    break
  for x in range(5):
    quest = str(input(f"\nEscolha a alternativa correta, {x}+1 = :\nA: 1\nB: 2\nC: 3\nD: 4\nE: 5 \nRESPOSTA: ")).upper().strip()[0]
    resposta.append(quest)
  for z in range(5):
    quest = str(input(f"\nEscolha a alternativa correta, 5-{z} = :\nA: 1\nB: 2\nC: 3\nD: 4\nE: 5 \nRESPOSTA: ")).upper().strip()[0]
    resposta.append(quest)

  for r in range(10):
    if resposta[r] == gabarito[r]:
      cont.append(1)
  nota.append(sum(cont))
  resposta.clear()
  cont.clear()
  perg = str(input("\nOutro aluno vai utilizar o sistema? (Sim ou Não): ")).upper().strip()[0]
  if perg == "N":
    break
print(f"{len(alunos)} Foi a quantidade de Alunos que participaram das provas.")
print(f"{max(nota)} Foi a maior das notas dos Alunos que participaram das provas.")
print(f"{min(nota)} Foi a menor das notas dos Alunos que participaram das provas.")
print(f"{sum(nota)/len(nota):.1f} Foi a media das notas dos Alunos que participaram das provas.")