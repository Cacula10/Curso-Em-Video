print('-' * 25)
print('{:^25}'.format('EXERCICIO 90'))
print('-' * 25)
nome = str(input('Nome: '))
media = float(input(f'Média do {nome}: '))
situacao = ' '
if media >= 6:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
dicionario = {'Nome': nome, 'Média': media, 'Situação': situacao}
print('-' * 25)
for k, v in dicionario.items():
    print(f'\033[1:31m{k:<10}\033[m é igual a \033[1:32m{v:>10}\033[m')



