num = float(input('Me diga um número qualquer: '))
if num % 2 == 0:
    print('O número \033[1;31m{:.0f}\033[m é \033[1;34mPAR'.format(num))
else:
    print('O número \033[1;31m{:.0f}\033[m é \033[1;32mÍMPAR'.format(num))