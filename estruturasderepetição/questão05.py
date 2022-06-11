# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

populaciona = float(input("Digite a população do Pais A: "))
populacionb = float(input("Digite a população do Pais B: "))
taxaa = float(input("Digite de crescimento anual do Pais A: "))
taxab = float(input("Digite de crescimento anual do Pais B: "))
anos = 0



while (populaciona < populacionb):
  percenta = (populaciona * taxaa) + populaciona
  percentb = (populacionb * taxab) + populacionb
  populaciona = percenta
  populacionb = percentb
  anos += 1
  
  if populaciona >= populacionb:
    print("{} Anos" .format(anos))
    print("População do Pais A: {:.2f}".format(populaciona))
    print("População do Pais B: {:.2f}".format(populacionb))
    break
