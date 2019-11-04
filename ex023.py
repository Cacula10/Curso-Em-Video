n = int(input('Informe um numero: '))
print('Analisando o numero {}'.format(n))
if n < 10:
    print('Unidade {}'.format(n))
if n >= 10 and n < 100:
    print('Unidade {}'.format(n % 10))
    print('Dezena  {}'.format(n // 10))
if n>= 100 and n < 1000:
    print('Unidade {}'.format(n % 100 % 10))
    print('Dezena  {}'.format(n % 100 // 10))
    print('Centena {}'.format(n // 100))
if n >= 1000 and n < 10000:
    print('Unidade {}'.format(n % 1000 % 10))
    print('Dezena  {}'.format(n % 1000 // 10 % 10))
    print('Centena {}'.format(n % 1000 // 100))
    print('Milhar  {}'.format(n // 1000))
