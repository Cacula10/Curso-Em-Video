print('*' * 15)
print('{:^15}'.format('EXERCICIO 085'))
print('*' * 15)
pilha = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o numero na posição {i}: '))
    if n % 2 == 0:
        pilha[0].append(n)
    else:
        pilha[1].append(n)
pilha[0].sort()
pilha[1].sort()
print(f'Os valores pares digitados foram {pilha[0]}')
print(f'Os valores impares digitados foram {pilha[1]}')
