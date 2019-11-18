print('\033[1;32m<>\033[m' * 35)
print('{:^70}'.format('\033[1;34mSISTEMA DE CONTROLE DE MÉDIA DE ALUNOS\033[m'))
print('\033[1;32m<>\033[m' * 35)
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1+nota2)/2
print('')
print('Tirando na primeira nota \033[1;32m{:.1f}\033[m e \033[1;32m{:.1f}\033[m na segunda\nMédia do aluno foi \033[1;32m{:.1f}\033[m'.format(nota1, nota2, media))
print('')
if media < 5:
    print('\033[1;36mREPROVADO.\033[m')
elif media >= 5 and media < 7:
    print('\033[1;36mRECUPERAÇÃO\033[m')
else:
    print('\033[1;32mAPROVADO!\033[m')