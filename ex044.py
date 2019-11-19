print('{:=^70}'.format('\033[1;34m LOJAS CAÇULA \033[m'))
produto = float(input('Preço da compra: R$ '))
print('''\033[1;34mFORMAS DE PAGAMENTO\033[m
[1] Á VISTA DINHEIRO/CHEQUE
[2] Á VISTA CARTÃO
[3] 2X CARTÃO
[4] 3 X OU MAIS NO CARTÃO
''')

opção = int(input('Qual opção? '))
if opção == 1:
    desconto = produto * 10/100
    print('\033[1;36m[1] Á VISTA DINHEIRO/CHEQUE...\033[m\nProduto: \033[1;34m{:.2f}\033[m\nDesconto: \033[1;34m{:.2f}\033[m\nCusto Final: \033[1;34m{:.2f}\033[m'.format(produto, desconto, produto - desconto))
elif opção == 2:
    desconto = produto * 5/100
    print('\033[1;36m[2] Á VISTA CARTÃO...\033[m\nProduto: \033[1;34m{:.2f}\033[m \nDesconto: \033[1;34m{:.2f}\033[m \nCusto Final: \033[1;34m{:.2f}\033[m '.format(produto, desconto, produto - desconto))
elif opção == 3:
    parcelas = produto / 2
    print('\033[1;36m[3] 2X CARTÃO - \033[1;34mSEM DESCONTO\033[m\n2 Parcelas: \033[1;34m{:.2f}\033[m \nCusto Final \033[1;34m{:.2f}\033[m'.format(parcelas, produto))
elif opção == 4:
    acrescimo = produto * 20/100
    qt_parcelas = int(input('Informe a quantidade de parcelas: '))
    print('\033[1;34m[4] 3 X OU MAIS NO CARTÃO...\033[m \nProduto: \033[1;34m{:.2f}\033[m \nAcrescimo: \033[1;34m{:.2f}\033[m \nCusto Final: \033[1;34m{:.2f}\033[m \nTotal Parcela: \033[1;34m{:.0f}\033[m'.format(produto, acrescimo, produto + acrescimo, (produto + acrescimo) / qt_parcelas))
else:
    print('\033[1;34mOPÇÃO INVÁLIDA...\033[m\nFAVOR INFORMAR UMAS DAS CONDIÇÕES INFORMADAS ACIMA...')