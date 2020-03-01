print('-' * 30)
print('{:^30}'.format('EXERCICIO 93'))
print('-' * 30)
gols = []
totalgol = 0
dicionario = dict()
nome = str(input('Nome do Jogador: ')).capitalize()
partidas = int(input(f'Quantas partidas o [{nome}] jogou? '))

for i in range(1, partidas+1):
    gols.append(int(input(f'Quantos gols na partida {i}: ')))
    totalgol += gols[i-1]
dicionario['Nome'] = nome
dicionario['Gols'] = gols
dicionario['Total'] = totalgol
print('=-' * 30)
print(dicionario)
print('=-' * 30)
for k, v in dicionario.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {dicionario["Nome"]} jogou {partidas} partidas.')
for i, v in enumerate(gols):
    print(f'=> Na partida {i+1} fez {v} gols')
print(f'Foi um total de {dicionario["Total"]} gols')