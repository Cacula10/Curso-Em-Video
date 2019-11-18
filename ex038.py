print('\033[1;35m<>\033[m' * 20)
print('{:^40}'.format('\033[1;32mCALCULANDO O MAIOR\033[m'))
print('\033[1;35m<>\033[m' * 20)
n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o segundo numero: '))
if n1 > n2:
    print('\033[1;34m{}\033[m é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('\033[1;32m{}\033[m é maior que {}'.format(n2, n1))
else:
    print('\033[1;31m{}\033[m e \033[1;31m{}\033[m são iguais'.format(n1, n2))