from time import sleep
from operator import itemgetter
dicti = dict()

dicti['Nome'] = str(input('Nome: '))
dicti['Média'] = float(input(f'Média de {dicti["Nome"]}: '))
if dicti['Média'] >= 7:
    dicti["Situação"] = "Aprovado"
elif dicti["Média"] >=5:
    dicti["Situação"] = "Exame"
else:
    dicti["Situação"] = "Reprovado"
print('=-' * 20)
for k, v in dicti.items():
    print(f'{k} = {v}')
print('=-' * 20)
