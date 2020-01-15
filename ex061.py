print('<>' * 20)
print('{:^40}'.format('\033[31mEXERCICIO 61\033[m'))
print('<>' * 20)
print('Gerador de uma PA')
print('\033[32m=\033[m' * 20)
pt = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
c = 0
while c < 10:
    if c == 0:
        print('{} >'.format(pt), end=' ')
    else:
        pt += razao
        print('{} > '.format(pt), end='')
    c += 1
print('\033[31m... ACABOU !\033[m', end=' ')