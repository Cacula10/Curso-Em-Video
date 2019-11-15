casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário ?'))
financiamento = int(input('Quantos anos deseja financiar o apto ?'))
prestacao = casa / (financiamento * 12)
print('Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de {:.2f}'.format(casa, financiamento, prestacao))
if prestacao > salario * (30/100):
    print('EMPRÉSTIMO NEGADO')
else:
    print('EMPRÉSTIMO CONCEDIDO')
