def leiaint(n):
    global numero
    numero = input(n)
    while not numero.isnumeric():
        print('\033[1:31mERRO!\033[m Digite um numero válido...')
        numero = input(n)


# Programa Principal
n = leiaint('Digite um numero: ')
#print(f'Você acabou de digitar o número {numero}')
