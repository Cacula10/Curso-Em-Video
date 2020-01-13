print('\033[31m*\033[m' * 35)
print("""\033[32mDigite um numero para
calcular o seu fatorial:\033[m """)
print('\033[31m*\033[m' * 35)
fatorial = int(input('Fatorial: '))
f = 1
c = fatorial
while c > 0:
    print('{}'.format(c), end=' ')
    if c > 1:
        print('x', end=' ')
    f *= c
    c -= 1
print('=', end=' ')
print(f, end=' ')



