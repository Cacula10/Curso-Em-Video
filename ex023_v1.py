n = int(input('Informe um numero: '))
unidade = n // 1 % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10
print('A unidade é {:.0f}'.format(unidade))
print('A dezena  é {:.0f}'.format(dezena))
print('A centena é {:.0f}'.format(centena))
print('A milhar  é {:.0f}'.format(milhar))
