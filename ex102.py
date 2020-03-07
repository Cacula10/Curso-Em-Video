def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um numero
    :param numero: O número a ser calculado
    :param show: (Opcional) Mostrar ou nao as contas
    :return: Retorna o valor do fatoria
    """
    contador = numero - 1
    while True:
        if show is True:
            print(f'{numero} X {contador}', end=' = ')
        numero *= contador
        contador -= 1
        if contador == 0:
            print(numero, end=' ')
            break


# Programa Principal
numero = int(input('Fatorial: '))
print(fatorial(numero))
help(fatorial)