# cabeçalho

print('\033[31m<>\033[m' * 35)
print('{:^70}'.format('\033[32mPESADO E LEVE\033[m'))
print('\033[31m<>\033[m' * 35)


for p in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))