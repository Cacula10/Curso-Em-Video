nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
media = (nota1+nota2)/2

if media < 5:
    print('Parabens burrão! foi reprovado.')
elif media < 6.9:
    print('quase burrão...ficou em recuperação')
else:
    print('APROVADO!')

print(media)