# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
perc = 0.015
val = int(input("Digite o salario inicial:"))
for sal in range(1996,2023):
  print(f'\nAno:{sal} \nValor:{(perc*val)+val:.2f}')
  print(f"Percentual: {perc:.2f}")
  val = (val*perc)+val
  if sal >= 1997:
    perc = (perc)*2