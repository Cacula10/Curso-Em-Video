print('-' * 25)
print('{:^25}'.format('EXERCICIO 90'))
print('-' * 25)
alunos = dict()
alunos['Nome'] = str(input('Nome: '))
alunos['Media'] = float(input(f'Média do {alunos["Nome"]}: '))
if alunos['Media'] >= 7:
    alunos['Situacao'] = 'Aprovado'
elif 5 <= alunos['Media'] <= 7:
    alunos['Situacao'] = 'Exame'
else:
    alunos['Situacao'] = 'Reprovado'
print('-' * 25)
for k, v in alunos.items():
    print(f'\033[1:31m{k:<10}\033[m é igual a \033[1:32m{v:>10}\033[m')



