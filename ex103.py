def ficha(jogador='<Desconhecido>', artilheiro = 0):
    print(f'O Jogador {jogador} fez {artilheiro} gol(s)')

nome = str(input('Nome do jogador: '))
gols = str(input('Quantos gols você fez: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(artilheiro=gols)
else:
    ficha(nome,gols)