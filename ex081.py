print('*' * 15)
print('{:^15}'.format('EXERCICIO 081'))
print('*' * 15)
lista = list()
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if continuar == 'N':
        print('<>' * 15)
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 not in lista:
    print(f'O valor 5 não faz parte da lista')
else:
    print(f'O valor 5 faz parte da lista')

