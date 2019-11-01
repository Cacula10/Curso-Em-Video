dias = int(input('Quantos dias alugados ?'))
km = float(input('Quantos km rodados ? '))
total = dias * 60 + (0.15 * km)
print('O total a pagar por {} dias e {}km rodados é: R${:.2f}'.format(dias, km, total))