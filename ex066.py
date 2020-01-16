print('<>' * 35)
print('{:^70}'.format('\033[31mEXERCICIO 66\033[m'))
print('<>' * 35)
soma = contador = 0
while True:
    valor = int(input('Digite uma valor [999 para parar]: '))
    if valor == 999:
        break
    soma += valor
    contador += 1
print(f'A soma dos {contador} valores é {soma}')
