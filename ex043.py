peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso Ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obeso')
else:
    print('Gordaço')