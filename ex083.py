print('*' * 15)
print('{:^15}'.format('EXERCICIO 083'))
print('*' * 15)
expressão = str(input('Digite a expressão: '))
pilha = list()
for simbolo in expressão:
    if simbolo == '(':
        pilha.append('(')
    else:
        if simbolo == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')
                break
if len(pilha) == 0:
    print('EXPRESSÃO VÁLIDA')
else:
    print('EXPRESSÃO INVÁLIDA')

