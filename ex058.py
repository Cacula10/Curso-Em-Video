# cabeçalho
print('\033[31m*\033[m' * 35)
print('{:^40}'.format('\033[32mEXERCICIO 058\033[m'))
print('\033[31m*\033[m' * 35)
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Será que consegue adivinhar qual foi ? ')

# importando bibilioteca
from random import randint
sorteio = randint(1, 10)

# variavel
contador = 1

# programa
palpite = int(input('Qual o seu palpite ? '))
while palpite != sorteio:
    if palpite > sorteio:
        print('Menos... Tente outra vez.')
    else:
        print('Mais... Tente outra vez.')
    contador += 1
    palpite = int(input('Qual o seu palpite? '))
print('Acertou com {} tentativa(s). Parabens !'.format(contador))

