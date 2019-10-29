from datetime import datetime
funcionario = dict()

funcionario["Nome"] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
funcionario["idade"] = datetime.now().year - nascimento
funcionario["CTPS"] = int(input('Carteira de Trabalho [0 não tem]: '))
if funcionario["CTPS"] != 0:
    funcionario["Contratação"] = int(input('Ano de Contratação: '))
    funcionario["Salário"] = float(input('Salário: '))
    funcionario["Aposentadoria"] = 35 - (datetime.now().year - funcionario["Contratação"] )
else:
    print(funcionario["Nome"])
    print(funcionario["idade"])
    print(funcionario["CTPS"])

for k, v in funcionario.items():
    print(f'{k} = {v}')
