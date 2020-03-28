def aumentar(numero=0, taxa=0, formatacao=False):
    resp = (numero * taxa) + numero
    return resp


def diminuir(numero=0, taxa=0, formatacao=False):
    resp = numero - (numero * taxa)
    return resp


def dobro(numero=0, formatacao=False):
    resp = numero * 2
    return resp


def metade(numero=0, formatacao=False):
    resp = numero/2
    return resp


def moeda(resp=0, moeda='R$'):# segundo parametro eu uso para fixar uma string "R$"
    return f'{moeda}{resp:.2f}'.replace('.', ',') # Retorno os paramentros na seguinte ordem "funcao" com R$ antes e depois o resp que é preço digitado que tambem coloco com duas casas decimais                                                # O replace eu substituo o ponto por virgula

