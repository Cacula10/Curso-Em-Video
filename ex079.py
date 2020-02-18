print('*' * 20)
print('{:^20}'.format('EXERCICIO 79'))
print('*' * 20)
lista = list()
cont = 0
while True:
        valor = int(input('Digite um valor: '))
        if valor in lista:
            print('\033[1:31mNumero Repetido ! Não vou adicionar na lista !\033[m')
        lista.append(valor)
        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Continuar [S/N]: ')).upper()[0]
        if continuar == 'N':
            break
        cont += 1
print('<>' * 30)
lista.sort()
print(lista)