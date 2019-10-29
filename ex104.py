def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO ! Digite um valor suave, não essa merda')
        if ok is True:
            break
    return valor


# Programa Principal
n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')
