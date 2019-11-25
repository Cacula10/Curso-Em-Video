print('=>' * 35)
print('{:^70}'.format('SOMA DOS NUMEROS PARES'))
print('=>' * 35)

soma = 0
cont = 0
for n in range(1, 7):
    numeros = int(input('informe o número {} : '.format(n)))
    if numeros % 2 == 0:
        cont += 1
        soma += numeros
print('A soma dos {} valores pares é {}'.format(cont, soma))

