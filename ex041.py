from datetime import date
from time import sleep
print('\033[1;35m<>\033[m' * 35)
print('{:^70}'.format('\033[1;34mCONFEDERAÇÃO DE NATAÇÃO\033[m'))
print('\033[1;35m<>\033[m' * 35)
nascimento = int(input('Ano de nascimento: '))
print('Calculando...')
sleep(2)
print('\033[1;35m<>\033[m' * 35)
atual = date.today().year
idade = atual - nascimento
print('O atleta tem \033[1;34m{}\033[m anos'.format(idade))
if idade <= 9:
    print('Categoria: \033[1;34mMIRIM\033[m')
elif idade <= 14:
    print('Categoria: \033[1;34mINFANTIL\033[m')
elif idade <= 19:
    print('Categoria: \033[1;34mJUNIOR\033[m')
elif idade <= 20:
    print('Categoria: \033[1;34mSENIOR\033[m')
else:
    print('Categoria: \033[1;34mMASTER\033[m')
