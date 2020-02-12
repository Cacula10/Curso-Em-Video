print('<>' * 15)
print('{:-^30}'.format('EXERCICIO 073'))
print('<>' * 15)
tabela = ('SANTOS','FLAMENGO','PALMEIRAS','ATLETICO MG','CORINTHIANS','INTERNACIONAL','SAO PAULO','ATLETICO PR','BOTAFOGO','CEARA','BAHIA','GREMIO','FORTALEZA','GOIAS','VASCO','FLUMINENSE','CRUZEIRO','CHAPECOENSE','CSA','AVAI')
print(f'Os cinco primeiros colocados do Brasileirão são: {tabela[:5]}')
print(f'Os quatro ultimos colocados do Brasileirão são: {tabela[-4:]}')
print(f'Os times em ordem alfabética: {sorted(tabela)}')
print('O time da Chapecoense está na posição', tabela.index('CHAPECOENSE') + 1, 'da tabela')

