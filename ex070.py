print('\033[1:31m=>\033[m' * 20)
print('{:^50}'.format('\033[1:32mEXERCICIO 070 - LOJA - BARATÃO\033[m'))
print('\033[1:31m=>\033[m' * 20)
totaldecompra = tot_mil = p_barato = contador = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preço = int(input('Preço: R$ '))
    contador += 1
    totaldecompra += preço
    if preço > 1000:
        tot_mil += 1
    if contador == 1 or preço < p_barato:
        p_barato = preço
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^50}'.format('\033[1:32mFIM DO PROGRAMA\033[m'))
print(f'O total de compra foi R${totaldecompra:.2f}')
print(f'Temos {tot_mil} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa {p_barato}')
