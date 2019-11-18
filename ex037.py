numero = int(input('Digite um numero inteiro: '))
print('\033[1;35m=>\033[m' * 40)
print('{:^80}'.format('\033[1;33mESCOLHA UMA DAS BASES PARA CONVERSÃO: \033[m'))
print('')
print('''[ 1 ] Converter para BINÁRIO
[ 2 ] Converver para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
print('\033[1;35m=>\033[m' * 40)
opção = int(input('sua opção: '))
while opção == '1' or '2' or '3':
    if opção == 1:
        print('CONVERTENDO PARA BINÁRIO: ', '\033[1;34m', bin(numero)[2:]), '\033[m'
        break
    elif opção == 2:
        print('CONVERTENDO PARA OCTAL: ', '\033[1;31m', oct(numero)[2:]), '\033[m'
        break
    elif opção == 3:
        print('CONVERTENDO PARA HEXADECIMAL', '\033[1;32m', hex(numero)[2:]), '\033[m'
        break
    else:
        opção = str(input('Opção inválida... Digite um valor entre [1 - 3]'))