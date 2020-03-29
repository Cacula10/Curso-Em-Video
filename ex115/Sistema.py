from ex115.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Criar Arquivo', 'Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Numero 1')
    elif resposta == 2:
        cabeçalho('Numero 2')
    elif resposta == 3:
        cabeçalho('Numero 3')
    elif resposta == 4:
        cabeçalho('Até logo...')
        break
    else:
        print('\033[1:31mErro! Favor digitar uma opção válida\033[m')
    sleep(2)
