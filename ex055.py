# cabeçalho

print('\033[31m<>\033[m' * 35)
print('{:^70}'.format('\033[32mGORDÃO E FININHO\033[m'))
print('\033[31m<>\033[m' * 35)

gordao = 0
fininho = 0

for pessoa in range(1, 5):
    peso = int(input('Peso da {} pessoa: '.format(pessoa)))
    if peso > gordao:
        gordao = peso
        fininho = peso
    elif peso < fininho:
        fininho = peso
print(gordao)
print(fininho)