from datetime import date
ano = int(input('Informe o ano que deseja que nós validemos ou coloque [0] para analisar o ano atual:  '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ANO {} É BISSESTO'.format(ano))
else:
    print('O ANO {} NÃO É BISSEXTO'.format(ano))