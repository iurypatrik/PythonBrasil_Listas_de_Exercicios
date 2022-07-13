# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

# basefixa = int(input("Digite um numero para Base: "))
# expoente = int(input("Digite um numero para Expoente: "))
# base = basefixa

# if expoente == 0:
#   print("Qualquer numero elevado a '0' é 1.")
# if expoente == 1:
#   print("Qualquer numero elevado a '1' é ele mesmo, ou seja,{}." .format(basefixa))
# if expoente < 0:
#   for num in range(1,(expoente*-1)):
#     base = base*basefixa
#     print(1/base)
  
# for num in range(1,expoente):
#   base = base*basefixa
#   print(base)



basefixa = int(input("Digite um numero para Base: "))
expoente = int(input("Digite um numero para Expoente: "))
base = basefixa

if expoente == 0:
  print("Qualquer numero elevado a '0' é 1.")
if expoente == 1:
  print("Qualquer numero elevado a '1' é ele mesmo, ou seja,{}." .format(basefixa))
if expoente < 0:
  for num in range(1,(expoente*-1)):
    base = base*basefixa
    print(1/base)
  
for num in range(1,expoente):
  base = base*basefixa
print("\033[32m{} \033[melevado a \033[32m{} \033[mé igual a \033[32m{}.".format(basefixa,expoente,base))
