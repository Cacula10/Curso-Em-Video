def fatorial(num=0,  show = False):
    """
    -> Calcular o fatorial de um numero
    :param num: O valor que deseja calcular o fatorial
    :param show: True or False para mostrar todos calculos
    :return: retornar o valor do fatoria do num
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show ==  True:
        print(f'{num}', end=' ')
        for c in range(num, 1, -1):
            print(f'x {c - 1}', end=' ')
        print('=', end=' ')
    return f


print(fatorial(5,show=True))
help(fatorial)