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



