print('{:=^60}'.format('\033[1;32m SOMA DOS PARES E MULTIPLOS DE TRÊS \033[m'))
s_impar = 0
c = 0
print('')
for i in range(1, 500):
    if i % 2 != 0 and i % 3 == 0:
        c += 1
        s_impar += i
print('\033[1;34mA soma de todos os \033[m\033[1;32m{}\033[m\033[1;34m valores solicitados é \033[m\033[1;32m{}\033[m'.format(c, s_impar))
