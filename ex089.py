lista = list()

while True:
    nome = str(input('Informe o seu nome: '))
    nota1 = float(input('Informe a sua nota1: '))
    nota2 = float(input('Informe a sua nota2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1,nota2],media])
    resp = str(input('Deseja continuar ? [S/N]'))
    if resp in 'Nn':
        print('FIM DE PROGRAMA...')
        break
print('-=' * 30)
print(f'{"Cod.":<5}{"Nome":<10}{"Media":>15}')
print('-=' * 25)

for i, n in enumerate(lista):
    print(f'{i:<5}{n[0]:<10}{n[2]:>15}')
print('*' * 25)
while True:
    opc = int(input('Digite o Cod. para notas ou [999] para encerrar: '))
    if opc == 999:
        print('FIM DE PROGRAMA')
        break
    if opc <= len(lista)-1:
        print(f'As notas de {lista[opc][0]} são {lista[opc][1]}')
print(lista)
