print('<>' * 15)
print('{:^30}'.format('EXERCICIO 078'))
print('<>' * 15)
cont = maior = menor = 0
lista = list()
posmenor = []
posmaior = []
for valor in range(1, 6):
    lista.append(int(input(f'Digite um valor para a posição {valor}:')))
    if cont == 0:
        maior = menor = lista[0]
        posmaior.append(1)
        posmenor.append(1)
        cont += 1
    for pos, p in enumerate(lista):
        if lista[pos] > maior:
            maior = lista[pos]
            posmaior.append(pos + 1)
            del posmaior[0]
        elif lista[pos] < menor:
            menor = lista[pos]
            posmenor.append(pos + 1)
            del posmenor[0]
print(f'Você digitou os valores \033[1:31m{lista}\033[m')

print(f'O maior numero que você digitou foi \033[1:31m{maior}\033[m nas posiçoes = ', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'\033[1:32m{i+1}\033[m', end=' ')
        print('...', end='')
print('')
print(f'O menor numero que você digitou foi \033[1:31m{menor}\033[m nas posições = ', end=' ')
for x, j in enumerate(lista):
    if j == menor:
        print(f'\033[1:32m{x+1}\033[m', end=' ')
        print('...', end=' ')