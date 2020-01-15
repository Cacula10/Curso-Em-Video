print('<>' * 20)
print('{:^40}'.format('\033[31mEXERCICIO 61\033[m'))
print('<>' * 20)
print('Gerador de uma PA')
print('\033[32m=\033[m' * 20)
pt = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
c = 0
opcao = 10
termo = 0
todos_termos = 0
while opcao != 0:
    termo = opcao
    while c < termo and opcao != 0:
        if c == 0:
            print('{} >'.format(pt), end=' ')
        if c > 0 and c < termo:
            pt += razao
            print('{} > '.format(pt), end='')
        c += 1
    print('\033[31m... PAUSA !\033[m', end=' ')
    print()
    opcao = int(input('Quantos termos você quer mostrar mais ? '))
    todos_termos += opcao
    c = 0
    pt = pt + razao
print('')
print('\033[32m=\033[m' * 20)
print('Progressão finalizado com \033[31m{}\033[m termos mostrados'.format(todos_termos + 10))
