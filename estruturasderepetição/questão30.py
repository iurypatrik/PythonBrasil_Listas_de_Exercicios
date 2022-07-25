# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
# Preço do pão: R$ 0.18
# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 50 - R$ 9.00

import numpy as np

pao = float(input("Digite o valor do pão: "))

preco = np.arange(0,101.49,pao)

qtd = int(input("Digite a quantidade de itens: "))

print(f"Você esta comprando {qtd} itens e sua conta deu R${preco[qtd]:.2f}")