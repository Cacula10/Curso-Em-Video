print('\033[1:32m<>\033[m' * 15)
print('{:-^30}'.format('EXERCICIO 075'))
print('\033[1:32m<>\033[m' * 15)
numeros = (int(input('Digite um numero: ')),
           int(input('Digite outro numero: ')),
           int(input('Digite mais um numero: ')),
           int(input('Digite o ultimo numero: ')))
print(f'Você digitou os valores: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 foi digitado na posição {numeros.index(3)+ 1}')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')