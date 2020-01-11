# cabeçalho
print('\033[31m*\033[m' * 35)
print('{:^40}'.format('\033[32mEXERCICIO 057\033[m'))
print('\033[31m*\033[m' * 35)
print('')

sexo = 'x'
sexo = str(input('Informe o seu sexo [M/F]: ')).strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).strip()[0]
print('Sexo {} registrado com sucesso'.format(sexo.upper()))