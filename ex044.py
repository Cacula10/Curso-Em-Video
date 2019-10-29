produto = float(input('Informe o valor do produto: '))
condição = str(input('Informe qual será a condição de pagamento: D,C,2x,3x: ')).upper()

if condição == 'D':
    print('DESCONTO R$:{:.2f} - O PRODUTO IRÁ CUSTAR R$: {:.2f}'.format(produto*0.1, produto-(produto*0.1)))
elif condição == 'C':
    print('DESCONTO R$: {:.2F} - O PRODUTO IRÁ CUSTAR R$: {:.2F}'.format(produto*0.05,produto - (produto*0.05)))
elif condição == '2X':
    print('NÃO POSSUÍ DESCONTO, O VALOR SERÁ O MESMO R$: {:.2F}'.format(produto))
elif condição == '3X':
    print('ACRESCIMO DE R$: {:.2F} - O PRODUTO IRÁ CUSTAR R$: {:.2F}'.format(produto*0.2, produto + (produto*0.2)))
else:
    print('FAVOR INFORMAR UMAS DAS CONDIÇÕES INFORMADAS ACIMA...')