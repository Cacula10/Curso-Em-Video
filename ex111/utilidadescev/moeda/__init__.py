def metade(valor=0, formatacao=False):
    resp = valor / 2
    return resp if formatacao is False else moeda(resp)


def dobro(valor=0, formatacao=False):
    resp = valor * 2
    return resp if formatacao is False else moeda(resp)


def aumentar(valor=0, taxa=0, formatacao=False):
    resp = valor + (valor * taxa)
    return resp if formatacao is False else moeda(resp)


def diminuir(valor=0, taxa=0, formatacao=False):
    resp = valor - (valor * taxa)
    return resp if formatacao is False else moeda(resp)


def moeda(valor=0, moeda='R$ '):
    """
    :param valor: Nesse parametro é o valor digitado pelo usuário na variavel preço
    :param moeda: Parametro que eu fixo o R$
    :return:  Retorno o preço formatado com R$ + ',' ao invez do '.'
    """
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor, aumento=0, diminui=0):
    """
    :param valor:  Preço digitado pelo usuario
    :param aumento: Taxa de aumento fixada em 10%
    :param diminui: Taxa de dimunuição fixada em 20%
    :return: não retorna nada... somente tabulamos e criamos um resumo de todas as "def"
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(valor)}')
    print(f'Dobro do Preço: \t{dobro(valor, True)}')
    print(f'Metade do Preço: \t{metade(valor, True)}')
    print(f'{aumento}% de Aumento: \t\t{aumentar(valor, aumento/100, True)}')
    print(f'{diminui}% de Redução: \t{diminuir(valor, diminui/100, True)}')
    print('-' * 30)
