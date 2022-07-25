# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

n = []
c = []
p = []
a = []

while True:
  cod = int(input("Digite seu codigo: "))
  if cod == 0:
    break
  nome = input("Digite seu nome: ")
  peso = float(input("Digite seu peso: "))
  altura = float(input("Digite seu altura: "))
  
  c.append(cod)
  n.append(nome)
  p.append(peso)
  a.append(altura)

# print(f'Codigo: {c}')
# print(f'Nome: {n}')
# print(f'Peso: {p}')
# print(f'Altura: {a}')

print(f'\nCliente mais Alto \nCodigo: {c[a.index(max(a))]}\nNome: {n[a.index(max(a))]}\nAltura: {max(a)}')
print(f'\nCliente mais Baixo \nCodigo: {c[a.index(min(a))]}\nNome: {n[a.index(min(a))]}\nAltura: {min(a)}')
print(f'\nCliente mais Gordo \nCodigo: {c[p.index(max(p))]}\nNome: {n[p.index(max(p))]}\nPeso: {max(p)}')
print(f'\nCliente mais Magro \nCodigo: {c[p.index(min(p))]}\nNome: {n[p.index(min(p))]}\nPeso: {min(p)}')


