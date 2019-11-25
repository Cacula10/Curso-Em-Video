print('=>' * 35)
print('{:^70}'.format('\033[1;34mSOMA DOS NUMEROS PARES\033[m'))
print('=>' * 35)

soma = 0
cont = 0
for n in range(1, 7):
    numeros = int(input('informe o número {} : '.format(n)))
    if numeros % 2 == 0:
        cont += 1
        soma += numeros
print('A soma dos {} valores pares é {}'.format(cont, soma))

