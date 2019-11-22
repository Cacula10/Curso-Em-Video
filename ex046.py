from time import sleep
print('{:=^50}'.format('\033[1;34m CONTAGEM REGRESSIVA \033[m'))
for i in range(10, -1, -1):
    sleep(0.5)
    print(i)
sleep(1)
print('POW POW PUM !!!')