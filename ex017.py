from math import hypot
coposto = float(input('Informe o valor do cateto oposto: '))
cadjacente = float(input('Inform o valor do cateto adjacente: '))
#hipotenusa = (coposto ** 2 + cadjacente ** 2) ** (1/2) -- outra forma de calcular

print('A hipotenusa vai medir {:.2f}'.format(hypot(coposto, cadjacente)))
