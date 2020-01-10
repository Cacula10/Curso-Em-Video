# cabeçalho
print('\033[32m*\033[m' * 35)
print('{:^40}'.format('\033[31mEXERCICIO 56\033[m'))
print('\033[32m*\033[m' * 35)

# Variaveis
somaidade = 0
idademaior = 0
velho = ''
qtdmulheres = 0

for i in range(1, 5):
    print('------- {} PESSOA -------'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).strip()
    if sexo in 'Mm' and i == 1:
        idademaior = idade
        velho = nome
    if idade > idademaior and sexo in 'Mm':
        idademaior = idade
        velho = nome
    if sexo in 'Ff' and idade < 20:
        qtdmulheres += 1
    somaidade += idade
    media = somaidade/i
print('{:^40}'.format('\033[31mRESULTADO\033[m'))
print('')
print('A média de idade do grupo é de \033[31m{}\033[m anos'.format(media))
print('O homem mais velho tem \033[31m{}\033[m anos e se chama \033[31m{}\033[m.'.format(idademaior, velho))
print('Ao todo \033[31m{}\033[m mulher(s) com menos de 20 anos'.format(qtdmulheres))


