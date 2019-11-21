from time import sleep
from random import choice

print('{:=^70}'.format('\033[1;33m JO\033[m\033[1;31m KEN\033[m \033[1;35mPO\033[m '))
print('''[1] PAPEL
[2] TESOURA
[3] PEDRA''')

lista = ['PAPEL', 'TESOURA', 'PEDRA']
pc = choice(lista)
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
    print('A sua jogada foi: {}'.format(escolha))
    print('Computador jogou: {}'.format(pc))
    print('EMPATE')
elif escolha == 1 and pc == 'PEDRA':
    print('A sua jogada foi: {}'.format('PAPEL'))
    print('Computador jogou: {}'.format(pc))
    print('VOCÊ VENCEU')
elif escolha == 1 and pc == 'TESOURA':
    print('A sua jogada foi: {}'.format('PAPEL'))
    print('Computador jogou: {}'.format(pc))
    print('VOCÊ PERDEU')
elif escolha == 2 and pc == 'PAPEL':
    print('A sua jogada foi: {}'.format('TESOURA'))
    print('Computador jogou: {}'.format(pc))
    print('VOCÊ VENCEU')
elif escolha == 2 and pc == 'PEDRA':
    print('A sua jogada foi: {}'.format('TEROURA'))
    print('Computador jogou: {}'.format(pc))
    print('VOCÊ PERDEU')
elif escolha == 3 and pc == 'TESOURA':
    print('A sua jogada foi: {}'.format('PEDRA'))
    print('Computador jogou: {}'.format(pc))
    print('VOCÊ VENCEU')
elif escolha == 3 and pc == 'PAPEL':
    print('A sua jogada foi: {}'.format('PEDRA'))
    print('Computador jogou: {}'.format(pc))
    print('VOCÊ PERDEU')
else:
    print('FAVOR DIGITAR UM NUMERO VÁLIDO')
print('=-' * 15)
