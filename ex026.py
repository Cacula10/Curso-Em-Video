frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase'.format(frase.upper().count('A')))
print('A primeira letra A apareceu na posiçao {}'.format(frase.upper().index('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.upper().rfind('A')+1))# nao considerou o espaço entre a frase
