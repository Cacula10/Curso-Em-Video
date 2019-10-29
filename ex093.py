futebol = dict()
artilharia = list()

futebol["Nome"] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {futebol["Nome"]} jogou ? '))

for c in range(0, partidas):
    artilharia.append(int(input(f'Quantos goals na partida {c+1}: ')))
futebol["goals"] = artilharia[:]
futebol["total"] = sum(artilharia)
print('=-' * 35)
print(futebol)
print('=-' * 35)
for k, v in futebol.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 35)
print(f'O jogador {futebol["Nome"]} jogou {partidas} partidas')

for i, v in enumerate(futebol["goals"]):
    print(f' => Na partida {i}, fez {v} goals')