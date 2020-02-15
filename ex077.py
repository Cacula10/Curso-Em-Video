print('*' * 30)
print('{:^30}'.format('EXERCICIO 077'))
print('*' * 30)
tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
         'PROGRAMADOR', 'FUTURO')

for p in tupla: # aqui nós varremos cada palavra da tupla
    print(f'Na palavra {p} temos:', end='')
    for letra in p: # aqui nós varremos cada letra de cada palavra
        if letra in 'AEIOU':
            print('\033[1:31m', letra, '\033[m', end='')
    print('')