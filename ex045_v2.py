# utilizado o RANDINT
from time import sleep
from random import randint

print('{:=^70}'.format('\033[1;33m JO\033[m\033[1;31m KEN\033[m \033[1;35mPO\033[m '))
print('''[0] PAPEL
[1] TESOURA
[2] PEDRA''')

itens = ['PAPEL', 'TESOURA', 'PEDRA']
pc = randint(0, 2)
escolha = int(input('QUAL SUA JOGADA? '))

sleep(1)
print('\033[1;32mJO\033[m', end='  ')
sleep(1)
print('\033[1;31mKEN\033[m', end='  ')
sleep(1)
print('\033[1;35mPO\033[m')
sleep(1)
print('=-' * 15)

if escolha == pc:
    print('A sua jogada foi: {}'.format(itens[escolha]))
    print('Computador jogou: {}'.format(itens[pc]))
    print('EMPATE')
elif escolha == 0 and pc == 2:
    print('A sua jogada foi: {}'.format('PAPEL'))
    print('Computador jogou: {}'.format(itens[pc]))
    print('VOCÊ VENCEU')
elif escolha == 0 and pc == 1:
    print('A sua jogada foi: {}'.format('PAPEL'))
    print('Computador jogou: {}'.format(itens[pc]))
    print('VOCÊ PERDEU')
elif escolha == 1 and pc == 0:
    print('A sua jogada foi: {}'.format('TESOURA'))
    print('Computador jogou: {}'.format(itens[pc]))
    print('VOCÊ VENCEU')
elif escolha == 1 and pc == 2:
    print('A sua jogada foi: {}'.format('TEROURA'))
    print('Computador jogou: {}'.format(itens[pc]))
    print('VOCÊ PERDEU')
elif escolha == 2 and pc == 0:
    print('A sua jogada foi: {}'.format('PEDRA'))
    print('Computador jogou: {}'.format(itens[pc]))
    print('VOCÊ PERDEU')
elif escolha == 2 and pc == 1:
    print('A sua jogada foi: {}'.format('PEDRA'))
    print('Computador jogou: {}'.format(itens[pc]))
    print('VOCÊ VENCEU')
else:
    print('FAVOR DIGITAR UM NUMERO VÁLIDO')
print('=-' * 15)
