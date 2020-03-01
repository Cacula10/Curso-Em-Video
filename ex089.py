print('-' * 25)
print('{:^30}'.format('\033[31mBOLETIM DE NOTAS\033[m'))
print('-' * 25)
lista = []
while True:
    nome = str(input('Digite o seu nome: '))
    nota1 = float(input('Digite a sua nota 01: '))
    nota2 = float(input('Digite a sua nota 02: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media]) # nesse momento eu ja salvo a lista da forma que desejo e da minha logica criada.
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
for i, v in enumerate(lista):
    print(f'{i} {v[0]:^33} {v[2]}', end=' ')
    print()
print('-' * 40)
opcao = 0
while True:
    opcao = int(input('Mostrar nota de qual aluno ? (999 para interromper): '))
    if opcao == 999:
        break
    if opcao <= len(lista) - 1:
        print(f'As notas do {lista[opcao][0]} são {lista[opcao][1]}')