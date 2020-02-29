print('-' * 25)
print('{:^25}'.format('\033[31mJOGO DA MEGA SENA\033[m'))
print('-' * 25)
from random import randint
from time import sleep
lista = []
lmega = []
palpite = int(input('Quantos sorteios da MEGA SENA, deseja fazer ? '))
total = 1
while total <= palpite:
    cont = 0 # esse contador precisa estar aqui para que ele seja zerado, após a lista estar preenchida. Senao o while d baixo nao vai ser executado na segunda vez, pois o "cont" ja é igual a "6"
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
        lista.sort()
    # a apartir daqui eu preciso adicionar meus dados em uma lista e depois apagar da lista
    # atencao na edentação, pois isso é feito no primeiro while la de cima.... apos ele ja ter criado o primeiro sorteio
    lmega.append(lista[:])
    lista.clear()
    total += 1
print('-' * 25)
print('{:^25}'.format('\033[1:31mRESULTADO DOS SEUS JOGOS\033[m'))
print('-' * 25)
for l, c in enumerate(lmega):
    print(f'Jogo {l+1} = {c}')
    sleep(1)
print('-' * 25)
print('BOA SORTE')