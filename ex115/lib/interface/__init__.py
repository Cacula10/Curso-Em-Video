def leiaint(num):
   while True:
       try:
            numeroint = int(input(num))
       except (ValueError, TypeError):
           print('\033[1:31mERRO! Por favor digite um numero inteiro válido!\033[m')
           continue
       else:
           return numeroint


def linha(tam=40):
    return '-' * tam


def cabeçalho(msg):
    print(linha())
    print(msg.center(40))
    print(linha())


def menu(lista):
    cabeçalho('\033[1:32mMENU PRINCIPAL\033[m')
    cont = 1
    for item in lista:
        print(f'\033[1:34m{cont}\033[m - \033[1:33m{item}\033[m')
        cont += 1
    print(linha())
    opc = leiaint('\033[1:37mSua Opção:\033[m ')
    return opc



