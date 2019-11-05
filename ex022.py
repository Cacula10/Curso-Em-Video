nome = str(input('Digite o seu nome completo: ')).strip()
separa = nome.split()
print('Analisando o seu nome...')
print('Seu nome em maisculo é: {}'.format(nome.upper()))
print('Seu nome em minusculo é: {}'.format(nome.lower()))
print('O seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

# nesse exercicio eu consigo ignorar os ESPAÇOS pois é uma conta com o uso do len, diferente do exercicio 26