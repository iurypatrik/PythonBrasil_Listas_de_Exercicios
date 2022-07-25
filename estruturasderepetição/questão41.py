# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67

vlrdivida = float(input("Digite o valor da divida: R$"))
parcela = int(input("Digite em quantos meses quer pagar: "))

if parcela >=1 and parcela <= 2:
  juros = 0
elif parcela >=3 and parcela <= 5:
  juros = 0.1
elif parcela >=6 and parcela <= 8:
  juros = 0.15
elif parcela >=9 and parcela <= 11:
  juros = 0.2
elif parcela == 12:
  juros = 0.25

vlrparcela = ((vlrdivida*juros)+vlrdivida)/parcela

print("\nvalor inicial da divida: R${}\nvalor do juros: {}%\nquantidade de parcelas: {}x\nvalor por parcela: R${:.2f}" .format(vlrdivida,(juros*100),parcela,vlrparcela))