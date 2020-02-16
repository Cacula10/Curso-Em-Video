print('<>' * 15)
print('{:^30}'.format('EXERCICIO 078'))
print('<>' * 15)
lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c+1}:')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'O maior valor foi \033[1:32m{maior}\033[m, nas posições ', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i+1}...', end=' ')
print('')
print(f'O menor valor foi \033[1:32m{menor}\033[m nas posições ', end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i+1}...', end=' ')