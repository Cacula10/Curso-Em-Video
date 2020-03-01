print('-' * 30)
print('{:^30}'.format('EXERCICIO 91'))
print('-' * 30)
print('{:^30}'.format('VALORES SORTEADOS'))
print('-' * 30)
from random import randint
from time import sleep
from operator import itemgetter
sorteio = list()
dicionario = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6),
              'Jogador 4': randint(1, 6)}
for k, v in dicionario.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.5)
print('-' * 30)
print('{:^30}'.format('RANKING DOS JOGADORES'))
print('-' * 30)
sorteio = sorted(dicionario.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(sorteio):
    print(f'{i+1} lugar ficou com {v[0]}')
    sleep(0.5)