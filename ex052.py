num = int(input('Digite um numero: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        cont += 1
    else:
        print('\033[m', end='')
    print(c, end=' ')
print('\033[m')
print('O numero \033[33m{}\033[m foi divisível \033[33m{}\033[m vezes'.format(num, cont))
if cont == 2:
    print('E por isso ele é \033[31mPRIMO\033[m')
else:
    print('E por isso ele não é \033[31mPRIMO\033[m')