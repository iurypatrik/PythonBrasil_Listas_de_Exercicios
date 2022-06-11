# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

# populaciona = 80000
# populacionb = 200000
# anos = 0
# while (populaciona < populacionb):
#   percenta = (populaciona * 0.030) + populaciona
#   percentb = (populacionb * 0.015) + populacionb
#   populaciona = percenta
#   populacionb = percentb
#   anos += 1
  
#   if populaciona >= populacionb:
#     print("{} Anos" .format(anos))
#     print("População do Pais A: {:.2f}".format(populaciona))
#     print("População do Pais B: {:.2f}".format(populacionb))
#     break


populaciona = 80000
populacionb = 200000
anos = 0
while True:
  #populaciona > populacionb
  percenta = (populaciona * 0.030) + populaciona
  percentb = (populacionb * 0.015) + populacionb
  populaciona = percenta
  populacionb = percentb
  anos += 1
  
  if populaciona >= populacionb:
    print("{} Anos" .format(anos))
    print("População do Pais A: {:.2f}".format(populaciona))
    print("População do Pais B: {:.2f}".format(populacionb))
    break