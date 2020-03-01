print('-' * 30)
print('{:^30}'.format('EXERCICIO 92'))
print('-' * 30)
from datetime import datetime
dicionario = dict()
while True:
    dicionario['Nome'] = str(input('Nome: '))
    nascimento = int(input('Ano de Nascimento: '))
    dicionario['Idade'] = datetime.now().year - nascimento
    dicionario['CTPS'] = str(input('Carteira de Trabalho (0 não tem): '))
    if dicionario['CTPS'] == '0':
        break
    dicionario['Contratacao'] = int(input('Ano de Contratação: '))
    dicionario['Salario'] = float(input('Sálario: '))
    dicionario['Aposentadoria'] = (35 - (datetime.now().year - dicionario["Contratacao"])) + datetime.now().year
    break
print('-' * 30)
for k, v in dicionario.items():
    print(f'\033[1:31m{k:<15}\033[m tem valor de \033[1:31m{v:>10}\033[m')