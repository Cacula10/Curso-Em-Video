lista = list()
temp = []
maiorp = menorp = 0

while True:
    temp.append(str(input('Informe o seu nome: ')))
    temp.append(float(input('Informe o seu peso: ')))
    if len(lista) == 0:
        maiorp = temp[1]
        menorp = temp[1]
    else:
        if temp[1] > maiorp:
            maiorp = temp[1]
        if temp[1] < menorp:
            menorp = temp[1]
    r = str(input('Deseja continuar [S/N]?'))
    lista.append(temp[:])
    del(temp[:])
    if r in 'Nn':
        break


print(f'Ao todo você cadastrou {len(lista)} pessoas')

print('{:-^40}'.format('TESTE DE FORMATAÇÃO COM PRINT'))

print(f'O maior peso foi {maiorp:.0f} e pertence > ',end=' ')
for peso in lista:
    if peso[1] == maiorp:
        print(f' ',peso[0],'...',end='')
print()

print('{:-^40}'.format('TESTE DE FORMATAÇÃO COM PRINT'))

print(f'O menor peso foi {menorp:.0f} e pertence > ', end=' ')
for peso in lista:
    if peso[1] == menorp:
        print(peso[0],'...',end='')
print()
print('{:-^40}'.format('FIM DE PROGRAMA'))