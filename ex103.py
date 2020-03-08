def ficha(nome='<<desconhecido>>', gol=0):
    print('-' * 20)
    global nomes, gols
    if len(nomes) > 0:
        if gols not in '0' and gols.isdigit():
            return f'O jogador {nomes} fez {gols} gols no campeonato'
        else:
            return f'O jogador {nomes} fez {0} gols no campeonato'
    elif len(nomes) == 0:
        if gols not in '0' and gols.isdigit():
            return f'O jogador <<desconhecido>> fez {gols} gols no campeonato'
        else:
            return f'O jogador <<desconhecido>> fez {0} gols no campeonato'
    else:
        return f'O jogador{nome} fez {gol} no campeonato'


# Programa Principal
nomes = str(input('Nome do Jogador: ')).capitalize()
gols = str(input('Numero de gols: '))
print(ficha(nomes, gols))

