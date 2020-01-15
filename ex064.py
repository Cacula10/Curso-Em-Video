print('\033[31m<>\033[m' * 15)
print('{:^30}'.format('EXERCICIO 64'))
print('\033[31m<>\033[m' * 15)
soma = n = contador = 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um numero [999 para parar]: '))
print('Você digitou {} numeros e a soma entre eles foi {}.'.format(contador, soma))
