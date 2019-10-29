futebol = dict()
artilharia = list()
clube = list()

while True:
    artilharia.clear()
    futebol["Nome"] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {futebol["Nome"]} jogou ? '))
    for c in range(0,partidas):
        artilharia.append(int(input(f'Quantos goals na partida {c+1}: ')))
    futebol["goals"] = artilharia[:]
    futebol["total"] = sum(artilharia)
    opc = str(input('Deseja continuar ? [S/N] ')).upper()[0]
    clube.append(futebol.copy())
    if opc == 'N':
        break
    if opc not in 'SN':
        opc = str(input('ERRO... Escolha S/N: ')).upper()[0]

print('=-' * 35)
print(clube)
print('=-' * 35)

print(f'{"Cod."}',end=' ')
for k in futebol.keys():
    print(f'{k:<15}',end=' ')
print()
print('=-' * 35)
for i, n in enumerate(clube):
    print(f'{i:<5}',end=' ')
    for d in n.values():
        print(f'{str(d):<15}',end=' ')
    print('')

while True:
    opc = int(input('Informe um numero da lista para detalhes: [999] para encerrar: '))
    if opc == 999:
        break
    elif opc >= len(clube):
        print(f'ERRO!  Não existe jogodor com o codigo de busca {opc} ')
    else:
        print(f'Levantamento de dados do jogador {clube[opc]["Nome"]}')

        for i, g in enumerate(clube[opc]['goals']):
            print(f'No jogo {i} fez {g} gols')