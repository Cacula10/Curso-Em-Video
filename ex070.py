print('\033[1:31m=>\033[m' * 20)
print('{:^50}'.format('\033[1:32mEXERCICIO 070 - LOJA - BARATÃO\033[m'))
print('\033[1:31m=>\033[m' * 20)

continuar = 'S'

while continuar is True:
    produto = str(input('Nome do Produto: ')).strip()
    preço = int(input('Preço: R$'))
    continuar = ' '
    while continuar not in 'SN':
        print('Favor digitar [S/N]')
        continuar = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

print('fim')
