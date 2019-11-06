from random import randint
from time import sleep
sorteio = randint(0, 5)
numero = float(input('Em que numero eu pensei ? '))

print('=>' * 45)
print('{:^90}'.format('Vou pensar em um numero entre 0 a 5. Tente adivinhar...'))
print('=>' * 45)
print('PROCESSANDO...')
print()
sleep(2)

if numero == sorteio:
    print('PARABENS... Você acertou! Pensamos no número {:.0f} '.format(numero))
else:
    print('GANHEI! Eu pensei no numero {:.0f} e não no {:.0f}!'.format(sorteio, numero))

