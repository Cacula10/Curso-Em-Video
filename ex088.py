print('-' * 40)
print('{:-^40}'.format('JOGO DA MEGA SENA'))
print('-' * 40)
print()
megasena = [[],[],[],[],[],[]]
from random import randint
from time import sleep
escolha = int(input('Informe quantos sorteios...'))

for i in range(escolha):
    for x in range(0,2):
        for y in range(0,2):
            megasena[x][y].append({randint(1,60)},{randint(1,60)})
        print()
print(megasena)

