from random import randint
# cabeçalho
print('\033[32m<>\033[m' * 20)
print('{:^40}'.format('\033[31mEXERCICIO 68\033[m'))
print('\033[32m<>\033[m' * 20)
print('-' * 40)
print('VAMOS JOGAR PAR OU ÍMPAR')
contador = 0

while True:
    print('')
    computador = randint(1, 10)
    usuário = int(input('Digite um valor: '))
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar [P/I]')).strip().upper()[0]
    soma = computador + usuário
    print('-' * 20)
    if soma % 2 == 0 and opcao == 'P':
        print(f'Você jogou {usuário} e o computador {computador}. Total de {soma} deu PAR')
        print('-' * 20)
        print('\033[32mVocê venceu !!!\033[m')
        contador += 1
    elif soma % 2 != 0 and opcao == 'I':
        print(f'Você jogou {usuário} e o computador {computador}. Total de {soma} deu ÍMPAR')
        print('-' * 20)
        print('\033[32mVocê venceu !!!\033[m')
        contador += 1
    else:
        print(f'Você jogou {usuário} e o computador {computador}. Total de {soma} deu', end=' ')
        if soma % 2 == 0:
            print('PAR')
        else:
            print('ÍMPAR')
        print('Você PERDEU!')
        print(f'GAME OVER, Você venceu \033[31m{contador}\033[m vez(s).')
        break

