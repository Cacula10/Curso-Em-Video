print('\033[1;31m=\033[m' * 70)
print('{:^70}'.format('\033[1;34m10 TERMOS DE UMA PA\033[m'))
print('\033[1;31m=\033[m' * 70)

t1 = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
décimo_termo = t1 + (10 - 1) * razao

print('\033[1;31m=\033[m' * 70)
print('')

for c in range(t1, décimo_termo + razao, razao):
    print('\033[1;34m', c, '\033[m', end='\033[1;31m...\033[m')
print(' \033[1;35mACABOU')
