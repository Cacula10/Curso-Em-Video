print('\033[1;34m*\033[m' * 80)
print('{:^110}'.format('\033[1;34m NUMEROS PARES DE\033[m \033[1;33m1 - 50\033[m \033[1;34mCOM LAÇO FOR \033[m'))
print('\033[1;34m*\033[m' * 80)
for i in range(2, 51, 2):
    print(i, end=' ')
print('FIM')