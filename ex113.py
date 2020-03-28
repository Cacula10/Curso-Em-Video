def leiafloat(num):
    while True:
        try:
            numeroreal = float(input('Digite um numero real: '))
        except (ValueError, TypeError):
            print('\033[1:31mERRO! Por favor digite um numero real válido!\033[m')
            continue
        else:
            return numeroreal


def leiaint(num):
   while True:
       try:
            numeroint = int(input(num))
       except (ValueError, TypeError):
           print('\033[1:31mERRO! Por favor digite um numero inteiro válido!\033[m')
           continue
       else:
           return numeroint


inteiro = leiaint('Digite um numero inteiro: ')
float = leiafloat('Digite um numero real: ')
print(f'O valor inteiro foi {inteiro} e o real foi {float}')






