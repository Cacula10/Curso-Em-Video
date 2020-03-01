print('-' * 25)
print('{:^30}'.format('\033[31mBOLETIM DE NOTAS\033[m'))
print('-' * 25)
lista = []
notas = []
boletim = []
while True:
    nome = str(input('Digite o seu nome: '))
    lista.append(nome)
    nota = int(input('Digite a sua nota 01: '))
    notas.append(nota)
    nota = int(input('Digite a sua nota 02: '))
    notas.append(nota)
    media = (notas[0] + notas[1]) / 2
    lista.append(notas[:])
    lista.append(media)
    boletim.append(lista[:])
    notas.clear()
    lista.clear()
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar ?')).upper()[0]
    if continua == 'N':
        break
print('-' * 40)

print('{:<10}'.format('ÍNDICE'), end=' ')
print('{:^15}'.format('NOME'), end=' ')
print('{:>10}'.format('MÉDIA', end=' '))
print()
for i, v in enumerate(boletim):
    print(f'{i} {v[0]:^33} {v[2]}', end=' ')
    print()
print('-' * 40)
opcao = 0
while True:
    opcao = int(input('Mostrar nota de qual aluno ? (999 para interromper): '))
    if opcao == 999:
        break
    print(f'As notas do {boletim[opcao][0]} são {boletim[opcao][1]}')