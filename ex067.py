print('\033[32m<>\033[m' * 20)
print('{:^40}'.format('\033[31mEXERCICIO 67\033[m'))
print('\033[32m<>\033[m' * 20)
contador = 1
while True:
    tabuada = int(input('Quer ver a tabuada de qual valor [digite um numero negativo para parar] ? '))
    if tabuada < 0:
        break
    print('-' * 20)
    while contador <= 10:
        print(contador, 'x', tabuada, '=', '\033[31m', contador*tabuada, '\033[m')
        contador += 1
    print('-' * 20)
    contador = 1
print('-' * 20)
print('\033[32mPROGRAMA DE TABUADA ENCERRADO. Volte Sempre !\033[m')