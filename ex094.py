pessoas = dict()
while True:
    pessoas["Nome"] = str(input('Nome: '))
    pessoas["Sexo"] = str(input('Sexo: [M/F]'))
    if pessoas["Sexo"] != "MmFf":
        print('valor errado... Favor digitar [M/F]')
    pessoas["Idade"] = int(input('Idade: '))
    opc = str(input('Quer continuar [S/N]: '))
    if opc in 'Nn':
        break
print(pessoas)