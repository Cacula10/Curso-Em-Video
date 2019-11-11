salario = float(input('Qual é o salário do funcionario: R$'))
if salario <= 1250:
    aumento = (salario * 0.15) + salario
else:
    aumento = (salario * 0.10) + salario

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, aumento))