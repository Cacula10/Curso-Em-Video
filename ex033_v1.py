a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = int(input('informe o terceiro valor: '))

menor = a
maior = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor é: {}'.format(menor))
print('O maior valor é: {}'.format(maior))