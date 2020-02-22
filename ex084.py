lista = list()
pilha = list()
maior = menor = 0
while True:
    lista.append(str(input('Digite o seu nome: ')))
    lista.append(float(input('Digite o seu peso: ')))
    if len(pilha) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    pilha.append(lista[:])
    lista.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [SN] ?')).upper()[0]
    if continuar == 'N':
        print('<>' * 20)
        break
print(f'Ao todo, você cadastrou {len(pilha)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ...', end=' ')
for p in pilha:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print('')
print(f'O menor peso foi de {menor}Kg. Peso de ...', end=' ')
for p in pilha:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print('')
