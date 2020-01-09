print('\033[31m=>\033[m' * 35)
print('{:^70}'.format('\033[32mCALCULO DE MAIOR IDADE\033[m'))
print('\033[31m=>\033[m' * 35)
print('')
# Variaveis
maior = 0
menor = 0

from datetime import datetime

atual = datetime.today().year

for i in range(0, 7):
    idade = int(input('Em que ano a {} pessoa nasceu ? '.format(i+1)))
    idade = atual - idade
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('\033[37m<>\033[m' * 35)
print('{:^70}'.format('\033[31mRESULTADO\033[m'))
print('\033[37m<>\033[m' * 35)
print('\033[32m{}\033[m pessoas maiores de idade'.format(maior))
print('\033[33m{}\033[m pessoas menores de idade'.format(menor))
