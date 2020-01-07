frase = str(input('Digite uma frase: ')).strip().upper()
dividida = frase.split()
juntada = ''.join(dividida)
# Outrao forma mais simples de fazer sem o uso do for >>>>>> inverso = juntada[-1::-1]
inverso = ''
for letra in range(len(juntada)-1, -1, -1):
    inverso += juntada[letra]

print('\033[31m=\033[m' * 35)
print('{:^35}'.format('\033[34mDESCOBRINDO UM PALINDROMO\033[m'))
print('\033[31m=\033[m' * 35)

if inverso == juntada:
    print('Essa frase é um \033[33mPALINDROMO\033[m')
else:
    print('Essa frase não é um \033[31mPALINDROMO\033[m')