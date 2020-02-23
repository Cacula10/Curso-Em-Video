print('*' * 15)
print('{:^15}'.format('EXERCICIO 086'))
print('*' * 15)
matriz = [[], [], []]
for pos in range(0, 3):
    n = int(input(f'Digite um valor para {0} {pos}: '))
    matriz[0].append(n)
for pos in range(0, 3):
    n = int(input(f'Digite um valor para {1} {pos}: '))
    matriz[1].append(n)
for pos in range(0, 3):
    n = int(input(f'Digite um valor para {2} {pos}: '))
    matriz[2].append(n)
for i, v in enumerate(matriz):
    print(v)