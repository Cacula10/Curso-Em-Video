print('*' * 15)
print('{:^15}'.format('EXERCICIO 082'))
print('*' * 15)
lista = list()
listp = list()
listi = list()
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        listp.append(n)
    else:
        listi.append(n)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N] ? ')).upper().strip()[0]
    if continuar in 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listp}')
print(f'A lista de impares é {listi}')