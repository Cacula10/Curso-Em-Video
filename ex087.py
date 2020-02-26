print('*' * 25)
print('{:^35}'.format('\033[1:32mEXERCICIO 087\033[m'))
print('*' * 25)
par = terceiracoluna = maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe um numero: {l} {c}: '))

for l in range(0, 3):
    terceiracoluna += matriz[l][2]
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print('')

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print('\033[1:32m*\033[m' * 25)

print(f'A soma dos valores pares é \033[1:31m{par}\033[m')
print(f'A soma dos valores da terceira coluna é \033[1:31m{terceiracoluna}\033[m')
print(f'A maior valor da segunda linha é: \033[1:31m{maior}\033[m')