matriz = [0,0,0],[0,0,0],[0,0,0]
soma = somacoluna = segundalinha = somapares = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}][{c}]: '))
        soma += matriz[l][c]
        somacoluna += matriz[l][2]
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]

for c in range(0, 3):
    for l in range(0, 3):
        if l == 0:
            segundalinha = matriz[1][l]
        else:
            if matriz[1][l] > segundalinha:
                segundalinha = (matriz[1][l])

for l in range(0,3):
    for c in range(0,3):
        print(matriz[l][c],end=' ')
    print()


print('{:-^40}'.format('RESPOSTAS'))
print(f'A soma de todos os valores é {soma}')
print('-'* 40)
print(f'A soma dos valores pares é: {somapares}')
print('-'*40)
print(f'A soma da terceira coluna é: {somacoluna}')
print('-'*40)
print(f'O maior valor da segunda linha é: {segundalinha}')
print()
print('{:-^40}'.format('FIM DO PROGRAMA'))