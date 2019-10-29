from datetime import date

nascimento = int(input('Favor informar o ano de seu nascimento: '))
idade = date.today().year
idade = idade - nascimento

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SENIOR')
else:
    print('MASTER')
print(idade, 'Anos')