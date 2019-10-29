from random import randint
from operator import itemgetter
sorteio = dict()

sorteio["1 Jogador"] = randint(1,6)
sorteio["2 Jogador"] = randint(1,6)
sorteio["3 Jogador"] = randint(1,6)
sorteio["4 Jogador"] = randint(1,6)

for k, v in sorteio.items():
    print(f'O {k} tirou {v} no dado')
print('=-' * 25)

sorteio2 = dict()

sorteio2 = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(sorteio2):
    print(f'O {k+ 1} colocado foi {v[0]} ele tirou no dado o valor {v[1]}')