# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = "a"
senha = 2
while nome != senha :
  nome = input("Digite seu nome: ")
  senha = input("Digite sua senha: ")
  if nome != senha:
    print("Error!")
  if nome == senha :
    print("Entrando...")
    break