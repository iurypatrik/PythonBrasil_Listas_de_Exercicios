# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite seu Nome: ")
idade = int(input("Digite seu Idade: "))
salario = float(input("Digite seu Salario: "))
sexo = input("Digite seu Sexo (f ou m): ")
estadocivil = input("Digite seu Estado Civil (s,c,v ou d): ")

if len(nome) > 3:
  print("Nome Valido")
else:
  print("Nome Invalido")

if idade >= 0 and idade <= 150:
  print("Idade Valida")
else:
  print("Idade Invalida")

if salario > 0:
  print("Salario Valido")
else:
  print("Salario Invalido")

if sexo == "f":
  print("Sexo Valido")
elif sexo == "m":
  print("Sexo Valido")
else:
  print("Sexo Invalido")

if estadocivil == "s":
  print("Estado Civil Valido")
elif estadocivil == "c":
  print("Estado Civil Valido")
elif estadocivil == "v":
  print("Estado Civil Valido")
elif estadocivil == "d":
  print("Estado Civil Valido")
else:
  print("Estado Civil Invalido")