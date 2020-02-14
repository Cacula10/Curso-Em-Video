print('*' * 33)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('*' * 33)
tabela = ('Lápis', 1.75,
          'Borracha', 0.50,
          'Caderno', 4.60,
          'Estojo', 25,
          'Transferidor', 4.20,
          'Compasso', 1.50,
          'Mochila', 30,
          'Caneta', 2,
          'Livro', 34.90)
for pos in range(0, len(tabela)):
    if pos % 2 == 0:
        print(f'{tabela[pos]:.<12}', end='')
    else:
        print('...............', end=' ')
        print(f'{tabela[pos]}')