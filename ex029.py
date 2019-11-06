velocidade = float(input('Em qual velocidade você está ? '))
multa80 = 7.0
if velocidade <= 80:
    print('Tenha um bom dia e diriga com segurança')
else:
    print('Você excedeu o limite de 80km/h !!!\nO valor da multa R${:.2f} reais'.format((velocidade - 80) * multa80))