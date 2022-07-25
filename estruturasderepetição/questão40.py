# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

pais = ["China","India","Nigeria","Brasil","Indonesia"]

veic = [207061286,114952000,12545177,64817974,72692951]

mort = [275983,231027,53339,42844,42734]

perc = []
for p in range(5):
  per = (mort[p]/veic[p])*100
  perc.append(per)

print(f"\nMaior Indice\nPais: {pais[perc.index(max(perc))]}\nIndice: {max(perc):.2f}%")
print(f"\nMenor Indice\nPais: {pais[perc.index(min(perc))]}\nIndice: {min(perc):.2f}%")
print(f"\nMedia de Veiculos por Pais: {sum(veic)/len(veic)}")

# medex = []
# for cont in range(5):
#   if veic[cont] < 2000:
#     medex.append(veic[cont])
# print(f"Media <2000 Habitantes: {sum(medex)/len(medex)}")


  