v1 = int(input('Informe o primeiro valor: '))
v2 = int(input('Informe o segundo valor: '))
v3 = int(input('Informe o terceiro valor: '))

maior = 0
menor = 0

if v1 > v2 and v1 > v3:
    maior = v1
    if v2 < v3:
        menor = v2
    else:
        menor = v3
elif v2 > v3 and v2 > v1:
    maior = v2
    if v1 < v3:
        menor = v1
    else:
        menor = v3
else:
    maior = v3
    menor = v1

print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))