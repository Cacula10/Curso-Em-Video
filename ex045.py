## PARA USAR O CHOICE DA BIBLIOTECA RAMNDOM PRECISO DE UMA LISTA
from random import choice

usuario = str(input('ESCOLHA (PAPEL),(TESOURA) OU (PEDRA): ')).upper()
lista = ['PAPEL', 'TESOURA', 'PEDRA']
maquina = choice(lista)

if maquina == usuario:
    print('JOGADA DA MAQUINA: {}'.format(maquina))
    print('JOGADA DO USUÁRIO:  {}'.format(usuario))
    print('EMPATE')
elif maquina == 'PAPEL' and usuario == 'PEDRA':
    print('JOGADA DA MAQUINA: {}'.format(maquina))
    print('JOGADA DO USUÁRIO:  {}'.format(usuario))
    print('MAQUINA VENCEU!!!')
elif maquina == 'PAPEL' and usuario == 'TESOURA':
    print('JOGADA DA MAQUINA: {}'.format(maquina))
    print('JOGADA DO USUÁRIO:  {}'.format(usuario))
    print('USUÁRIO VENCEU')
elif maquina == 'PEDRA' and usuario == 'TESOURA':
    print('JOGADA DA MAQUINA: {}'.format(maquina))
    print('JOGADA DO USUÁRIO:  {}'.format(usuario))
    print('MAQUINA VENCEU')
elif maquina == 'PEDRA' and usuario == 'PAPEL':
    print('JOGADA DA MAQUINA: {}'.format(maquina))
    print('JOGADA DO USUÁRIO:  {}'.format(usuario))
    print('USUÁRIO VENCEU')
elif maquina == 'TESOURA' and usuario == 'PEDRA':
    print('JOGADA DA MAQUINA: {}'.format(maquina))
    print('JOGADA DO USUÁRIO:  {}'.format(usuario))
    print('USUÁRIO VENCEU')
elif maquina == 'TESOURA' and usuario == 'PAPEL':
    print('JOGADA DA MAQUINA: {}'.format(maquina))
    print('JOGADA DO USUÁRIO:  {}'.format(usuario))
    print('MAQUINA VENCEU')
else:
    print('JOGA DIREITO ANIMAL')

