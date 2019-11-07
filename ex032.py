from datetime import date

print('\033[1;32m*' * 70)
print('{:^70}'.format('\033[1;34mANÁLISE DE ANO BISSEXTO\033[m'))
print('\033[1;32m*\033[m' * 70)
ano = int(input('Informe o ano que deseja que nós validemos ou coloque [0] para analisar o ano atual:  '))
atual = date.today().year
if ano == 0:
    ano = atual
    if ano % 4 == 0:
        if ano % 100 != 0:
            print('{} = BISSEXTO'.format(ano))
        elif ano % 100 == 0:
            if ano % 400 == 0:
                print('{} = BISSEXTO E DIVISAO EXATA POR 400'.format(ano))
            else:
                print('{} = NÃO É UM ANO BISSEXTO'.format(ano))
    else:
        print('{} = NÃO É UM ANO BISSEXTO'.format(ano))
else:
    if ano % 4 == 0:
        if ano % 100 != 0:
            print('{} = BISSEXTO'.format(ano))
        elif ano % 100 == 0:
            if ano % 400 == 0:
                print('{} = BISSEXTO E DIVISAO EXATA POR 400'.format(ano))
            else:
                print('{} = NÃO É UM ANO BISSEXTO'.format(ano))
    else:
        print('{} = NÃO É UM ANO BISSEXTO'.format(ano))

