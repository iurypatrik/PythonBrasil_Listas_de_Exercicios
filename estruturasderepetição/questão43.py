# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

esp = ["Cachorro Quente","Bauru Simples","Bauru com ovo","Hambúrguer","Cheeseburguer","Refrigerante"]
cod = [100,101,102,103,104,105]
preco = [1.2,1.3,1.5,1.2,1.3,1]

pedido = []
qtdpedido = []
totgeral = []

while True:
  item = int(input("Digite o codigo do item que deseja: "))
  if item < 100 or item > 105:
    print("Pedido Encerrado!")
    break
  qtd = int(input("Digite a quantidade: "))
  pedido.append(item)
  qtdpedido.append(qtd)

print("\nRESUMO DO PEDIDO")
for c in range(len(pedido)):
  print(f"\nItem{c+1}:{esp[cod.index(pedido[c])]}\nCodigo:{pedido[c]}\nValor:R${preco[cod.index(pedido[c])]*qtdpedido[c]:.2f}")
  totgeral.append(preco[cod.index(pedido[c])]*qtdpedido[c])
  
print(f"\nTotal Geral:R${sum(totgeral):.2f}")
