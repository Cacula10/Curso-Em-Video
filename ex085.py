lista = [[],[]]
npar = nimpar = 0

for c in range(0,7):
    n = int(input(f'Informe {c} numero: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Os numeros pares: {lista[0]}')
print(f'Os numeros impares: {lista[1]}')

