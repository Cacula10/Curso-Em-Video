print('-' * 30)
print('{:^30}'.format('EXERCICIO 95'))
print('-' * 30)
dictjogaodores = dict()
listagols = list()
listajogadores = list()
totalgols = 0
while True:
    dictjogaodores.clear() # O ideal é fazer a limpeza aqui na parte de cima
    listagols.clear()
    dictjogaodores['Nome'] = str(input('Nome do Jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas \033[1:34m{dictjogaodores["Nome"]}\033[m jogou ? '))
    for i in range(1, partidas+1):
        listagols.append(int(input(f'Quantos gols na partida {i+1}: ')))
    dictjogaodores['Gols'] = listagols[:]
    dictjogaodores['Total'] = sum(listagols)
    listajogadores.append(dictjogaodores.copy())
    while True:
        continuar = str(input('Quer continuar [S/N] ? ')).upper()[0]
        if continuar in 'SN': # enquanto ele nao colococar S ou N "print" o "Erro!" Senao ele sai desse while True
            break
        print('Erro! Responda apenas S ou N')
    if continuar == 'N':
        break
# Finalização do código de imput

print('-' * 80)
print('Cod', end=' ')
for i in dictjogaodores.keys():
    print(f'{i:<20}', end=' ')
print()
print('-' * 80)
for k, v in enumerate(listajogadores):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<20}', end=' ')# para exibição de "d" precisa converter para "str".
    print()
while True:
    opc = int(input('Mostrar dados de qual jogador (999 para interromper): '))
    if opc == 999:
        break
    if opc >= len(listajogadores):
        print(f'ERRO! Não existe jogador com esse código de busca {opc}')
    else:
        print(f'Levantamento de dados do jogaoor {listajogadores[opc]["Nome"]}')
        for i, g in enumerate(listajogadores[opc]["Gols"]):# Aqui eu acesso uma lista dentro de um dicionario e dentro de uma outra lista
            print(f'No jogo {i+1} fez {g} gols.')
    print('-' * 80)
print('<<<FIM>>>')