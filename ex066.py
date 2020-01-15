print('\033[31m=<\033[m' * 20)
print('{:^40}'.format('EXERCICIO 66 - FIBONACCI'))
print('\033[31m=<\033[m' * 20)
termos = int(input('Quantos termos você quer mostrar ? '))
print('\033[32m<>\033[m' * 20)

contador = 0
a = 1
b = 1
c = 2
while contador <= termos:
    if contador == termos:
        break
    print('{} > '.format(a), end='')
    a = b + c
    contador += 1
    if contador == termos:
        break
    print('{} >'.format(b), end=' ')
    b = a + c
    contador += 1
    if contador == termos:
        break
    print('{} >'.format(c), end=' ')
    c = b + a
    contador += 1
print('FIM')