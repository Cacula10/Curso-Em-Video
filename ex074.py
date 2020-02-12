from random import randint
print('\033[1:31m<>\033[m' * 15)
print('{:^30}'.format('EXERCICIO 074'))
print('\033[1:31m<>\033[m' * 15)
sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = menor = sorteio[0]
contador = 1

while True:
    if sorteio[contador] >= maior:
        maior = sorteio[contador]
    if sorteio[contador] <= menor:
        menor = sorteio[contador]
    contador += 1
    if contador == 5:
        break
print(f'Os valores sorteados foram: \033[1:31m{sorteio}\033[m')
print(f'O maior valor do sorteio foi \033[1:31m{maior}\033[m e o menor \033[1:31m{menor}\033[m')