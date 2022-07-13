# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';


cont = 0
while cont != 5:
  for c in range(2):
    nome = input("\n\033[mDigite seu Nome: ")
    if len(nome) > 3:
      cont+=1
      break
    else:
      print("\n\033[31mNome incorreto! Você usou {} chance." .format(c+1))
  for c in range(2):
    salario = float(input("\n\033[mDigite seu Salario: "))
    if salario > 0:
      cont+=1
      break
    else:
      print("\n\033[31mSalario incorreto! Você usou {} chance." .format(c+1))
  for c in range(2):
    idade = int(input("\n\033[mDigite seu Idade: "))
    if idade >= 0 and idade <= 150:
      cont+=1
      break
    else:
      print("\n\033[31mIdade incorreta! Você usou {} chance." .format(c+1))
  for c in range(2):
    sexo = str(input("\n\033[mDigite seu Sexo\033[33m(M ou F):\033[m")).upper().strip()[0]
    if sexo in "FM":
      cont+=1
      break
    else:
      print("\n\033[31mSexo incorreto! Você usou {} chance." .format(c+1))
  for c in range(2):
    estadocivil = str(input("\n\033[mDigite seu Estado Civil\033[33m(S,C,V ou D):\033[m")).upper().strip()[0]
    if estadocivil in "SCVD":
      cont+=1
      break
    else:
      print("\n\033[31mEstado Civil incorreto! Você usou {} chance." .format(c+1))
  if cont != 5:
    break
#----------------------------------------
    
if len(nome) > 3:
  print("\n\033[32mNome '{}' --> Valido!".format(nome))
else:
  print("\n\033[31mNome '{}' --> Invalido!".format(nome))

if idade >= 0 and idade <= 150:
  print("\n\033[32mIdade '{}' --> Valida!".format(idade))
else:
  print("\n\033[31mIdade '{}' --> Invalida!".format(idade))

if salario > 0:
  print("\n\033[32mSalario '{}' --> Valido!".format(salario))
else:
  print("\n\033[31mSalario '{}' --> Invalido!".format(salario))

if sexo in "FM":
  print("\n\033[32mSexo '{}' --> Valido!".format(sexo))
else:
  print("\n\033[31mSexo '{}' --> Invalido!".format(sexo))

if estadocivil in "SCVD":
  print("\n\033[32mEstado Civil '{}' --> Valido!".format(estadocivil))
else:
  print("\n\033[31mEstado Civil '{}' --> Invalido!".format(estadocivil))






# cont = 0
# while cont != 5:
#   for c in range(2):
#     nome = input("\n\033[mDigite seu Nome: ")
#     if len(nome) > 3:
#       cont+=1
#       break
#     else:
#       print("\n\033[31mNome incorreto! Você usou {} chance." .format(c+1))
#   for c in range(2):
#     salario = float(input("\n\033[mDigite seu Salario: "))
#     if salario > 0:
#       cont+=1
#       break
#     else:
#       print("\n\033[31mSalario incorreto! Você usou {} chance." .format(c+1))
#   for c in range(2):
#     idade = int(input("\n\033[mDigite seu Idade: "))
#     if idade >= 0 and idade <= 150:
#       cont+=1
#       break
#     else:
#       print("\n\033[31mIdade incorreta! Você usou {} chance." .format(c+1))
#   for c in range(2):
#     sexo = input("\n\033[mDigite seu Sexo\033[33m(f ou m):\033[m")
#     if sexo == "f" or sexo == "m":
#       cont+=1
#       break
#     else:
#       print("\n\033[31mSexo incorreto! Você usou {} chance." .format(c+1))
#   for c in range(2):
#     estadocivil = input("\n\033[mDigite seu Estado Civil\033[33m(s,c,v ou d):\033[m")
#     if estadocivil == "s" or estadocivil == "c" or estadocivil == "v" or estadocivil == "d":
#       cont+=1
#       break
#     else:
#       print("\n\033[31mEstado Civil incorreto! Você usou {} chance." .format(c+1))
#   if cont != 5:
#     break
# #----------------------------------------
    
# if len(nome) > 3:
#   print("\n\033[32mNome '{}' --> Valido!".format(nome))
# else:
#   print("\n\033[31mNome '{}' --> Invalido!".format(nome))

# if idade >= 0 and idade <= 150:
#   print("\n\033[32mIdade '{}' --> Valida!".format(idade))
# else:
#   print("\n\033[31mIdade '{}' --> Invalida!".format(idade))

# if salario > 0:
#   print("\n\033[32mSalario '{}' --> Valido!".format(salario))
# else:
#   print("\n\033[31mSalario '{}' --> Invalido!".format(salario))

# if sexo == "f" or sexo == "m":
#   print("\n\033[32mSexo '{}' --> Valido!".format(sexo))
# else:
#   print("\n\033[31mSexo '{}' --> Invalido!".format(sexo))

# if estadocivil == "s" or estadocivil == "c" or estadocivil == "v" or estadocivil == "d":
#   print("\n\033[32mEstado Civil '{}' --> Valido!".format(estadocivil))
# else:
#   print("\n\033[31mEstado Civil '{}' --> Invalido!".format(estadocivil))
