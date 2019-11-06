distancia = float(input('Qual a distância da sua viagem? '))
p_menor200km = distancia * 0.50
p_maior200km = distancia * 0.45
print('Você está prestes a fazer uma viagem de {:.0f}km'.format(distancia))
if distancia <= 200:
    print('O preço da sua passagem será de R${:.2f}'.format(p_menor200km))
else:
    print('O preço da sua passagem será de R${:.2f}'.format(p_maior200km))


