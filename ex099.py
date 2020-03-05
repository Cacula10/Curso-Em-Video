from time import sleep



def desempacotando(*num):
    cont = maior = 0
    print('<>' * 25)
    print('Analisando os valores passados...')
    sleep(0.5)
    for v in num:
        print(f'[{v}]', end=' ')
        if cont == 0:
            maior = v
            cont += 1
        else:
            if v > maior:
                maior = v
    print(' FIM')
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')


#Programa principal
desempacotando(11, 13, 12, 39, 34, 22)
desempacotando(1, 3, 22, 111)
desempacotando(0)
desempacotando()