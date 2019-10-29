from time import sleep

def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'contagem de {i} até {f} de {p} até {p}')
    if i < f:
        c = 1
        while c <= f:
            print(f'{c}',end=' ')
            sleep(0.5)
            c += p
        print('FIM')
    else:
        c = i
        while c >= f:
            print(f'{c}',end=' ')
            sleep(0.5)
            c -= p
        print('FIM')

contador(1,10,1)
contador(10,0,2)

print('Agora é sua vez de personalizar a contagem: ')
ini = int(input('Inicio:  '))
fim = int(input('Fim:     '))
passo = int(input('Passo: '))
contador(ini,fim,passo)


