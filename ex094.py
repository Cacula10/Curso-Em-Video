print('-' * 30)
print('{:^30}'.format('EXERCICIO 94'))
print('-' * 30)
dicionario = dict()
lista = list()
somaidade = média = 0
while True:
    dicionario['Nome'] = str(input('Nome: '))
    dicionario['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    while dicionario['Sexo'] not in 'MF':
        dicionario['Sexo'] = str(input('Por favor digite apenas [M/F]: ')).upper()[0]
    dicionario['Idade'] = int(input('Idade: '))
    somaidade += dicionario['Idade']
    lista.append(dicionario.copy())
    continuar = str(input('Deseja continuar [S/N]: ')).upper()
    while continuar not in 'SN':
        print('Erro! Digite apenas [S/N]')
        continuar = str(input('Deseja continuar [S/N]: ')).upper()
    if continuar == 'N':
        break
    média = somaidade / len(lista)
print('-' * 30)
print(f'A) Ao todo temos \033[1:32m{len(lista)}\033[m pessoas cadastradas.')
print(f'B) A média de idade é \033[1:31m{somaidade/len(lista):.0f}\033[m')
print(f'C) As mulheres cadastradas...', end='')
for v in lista:
    if v['Sexo'] == 'F':
        print(f'\033[1:35m[{v["Nome"]}]\033[m', end='  ')
print()
print(f'D) Lista de pessoas que está acima da média de idade: ')
for v in lista:
    if v['Idade'] >= média:
        print(f'\033[1:34m{v}\033[m')