from time import sleep
print('\033[1;34m=-\033[m' * 35)
print('{:^70}'.format('\033[1;35mCALCULO DO IMC\033[m'))
print('\033[1;34m=-\033[m' * 35)

peso = float(input('Informe seu peso: (Kg) '))
altura = float(input('Informe sua altura: (m) '))
imc = peso / (altura ** 2)

print('\033[1;34m*\033[m' * 35)
print('\033[1;35mCalculando...\033[m')
sleep(2)
print('\033[1;34m*\033[m' * 35)
if imc < 18.5:
    print('O seu IMC é: {:.1f} = '.format(imc), end='')
    print('MAGREZA')
elif imc < 25:
    print('O seu IMC é: {:.1f} = '.format(imc), end='')
    print('NORMAL')
elif imc < 30:
    print('O seu IMC é: {:.1f} = '.format(imc), end='')
    print('SOBREPESO')
elif imc < 40:
    print('O seu IMC é {:.1f} = '.format(imc), end='')
    print('OBESIDADE')
else:
    print('O seu IMC é {:.1f} = '.format(imc), end='')
    print('OBESIDADE GRAVE')