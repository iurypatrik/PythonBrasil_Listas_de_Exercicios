# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = "a"
senha = 2
while nome != senha :
  nome = input("\033[mDigite seu nome: ")
  senha = input("\033[mDigite sua senha: ")
  if nome != senha:
    print("\033[31mUsuario ou Senha incorretos! Tente Novamente...")
  if nome == senha :
    print("\033[32mEntrando...")
    break