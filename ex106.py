from time import sleep
cores = ('\033[m',
         '\033[1:31m',
         '\033[1:32m',
         '\033[1:33m'
         )

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 2)
    print(cores[0], end=' ')
    help(com)
    print(cores[0], end=' ')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end=' ')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(cores[0], end=' ')
    sleep(2)


# Programa Principal
comando = ' '
while True:
    titulo('SISTEMA DE AJUDA [Py-Help]', 1)
    comando = str(input('Função ou Biblioteca > [FIM PARA PARAR]: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)