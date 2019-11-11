print('\033[1;31m-=\033[m' * 25)
print('{:^50}'.format('\033[1;34m Analisando um triangulo\033[m'))
print('\033[1;31m-=\033[m' * 25)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < (b + c) and b < (a + c) and c < (a + b):
    print('Os segmentos informados \033[1;34mPODEM\033[m formar um triangulo')
else:
    print('Os segmentos informados \033[1;35mNAO PODEM\033[m formar um triangulo')