def leiadinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or len(entrada) == 0:
            print(f'ERRO! "{entrada}" não é válido')
        else:
            return float(entrada)
