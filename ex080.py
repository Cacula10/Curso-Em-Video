print('<>' * 10)
print('{:^10}'.format('EXERCICIO 080'))
print('<>' * 10)
lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Valor adicionado na ultima posição')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos+1}')
                break
            pos += 1
print(lista)
