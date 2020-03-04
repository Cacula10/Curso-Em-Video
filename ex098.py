from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('=>' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)
    if i < f:
        for c in range(i, f+1, p):
            print(f'{c}', end=' ')
            sleep(0.2)
        print('FIM')
    else:
        for c in range(i, f-p, -p):
            print(f'{c}', end=' ')
            sleep(0.2)
        print('FIM')


# Programa Principal 3
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem: ')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)