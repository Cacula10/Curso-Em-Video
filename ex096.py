print('-' * 30)
print('{:^30}'.format('EXERCICIO 96'))
print('-' * 30)
def área(l, c):
    area = l * c
    print(f'A área de um terreno {l}x{c} é de {area} metros quadrado')

# PROGRAMA PRINCIPAL
print('Controle de Terrenos')
print('--------------------')
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
área(largura, comprimento)