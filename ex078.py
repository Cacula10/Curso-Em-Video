lista = []
maior = 0
menor = 0

for cont in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {cont}: ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print(f'A lista de valores ficou {lista}')
print(f'O maior valor {maior} e esta na posição',end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f' {i}...',end='')
    if v == menor:
        print(f'{i}...',end='')
print()