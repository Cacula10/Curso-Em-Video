# cabeçalho
print('\033[31m<>\033[m' * 15)
print('{:^35}'.format('\033[32mEXERCICIO 59\033[m'))
print('\033[31m<>\033[m' * 15)
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA')
    opcao = int(input('>>>>>> QUAL A SUA OPÇÃO ? '))
    print('*' * 35)
    if opcao == 1:
        print('A soma entre {} + {} é {}'.format(v1, v2, v1+v2))
    elif opcao == 2:
        print('O resultado de {} x {} é {}'.format(v1, v2, v1*v2))
    elif opcao == 3:
        if v1 > v2:
            print('Entre {} e {} o maior valor é {}'.format(v1, v2, v1))
        else:
            print('Entre {} e {} o maior valor é {}'.format(v1, v2, v2))
    elif opcao == 4:
        print('informe os numeros novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    else:
        print('Opção inválida! Tente novamente!')

print('FINALIZANDO...')
print('*' * 35)
print('Fim do programa! Volte sempre!')
