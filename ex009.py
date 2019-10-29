n = int(input('Digite um numero para ver a sua tabuada: '))
p = n * 1
s = n * 2
t = n * 3
q = n * 4
qu = n * 5
print(16*'-')
print('1 X {} = {} \n2 X {} = {} \n3 X {} = {} \n4 X {} = {} \n5 X {} = {}'.format(n, p, n, s, n, t, n, q, n, qu))
print(16*'-')

numero = int(input('Digite outro numero para ver a tabuada: '))
print('{} X {:2} = {}'.format(numero, 1, (numero*1)))
print('{} X {:2} = {}'.format(numero, 2, (numero*2)))
print('{} X {:2} = {}'.format(numero, 10, (numero*10)))
