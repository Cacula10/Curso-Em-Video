# cabeçalho
print('\033[32m<>\033[m' * 25)
print('{:^50}'.format('\033[31mEXERCICIO 65\033[m'))
print('\033[32m<>\033[m' * 25)

continua = 's'
contador = média = soma = maior = menor = 0

while continua not in 'Nn':
    numero = int(input('Digite um número: '))
    continua = str(input('Quer continuar : [S/N]'))
    soma += numero
    if contador == 0:
        maior = menor = numero
    else:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
    contador += 1
    média = soma / contador

print('Você digitou \033[31m{}\033[m numeros e a media foi \033[31m{}\033[m'.format(contador, média))
print('O maior valor foi \033[31m{}\033[m e o menor \033[31m{}\033[m.'.format(maior, menor))


