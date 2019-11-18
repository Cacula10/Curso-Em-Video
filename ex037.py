numero = int(input('Digite um numero inteiro: '))
print('\033[1;35m=>\033[m' * 40)
print('{:^80}'.format('\033[1;33mESCOLHA UMA DAS BASES PARA CONVERSÃO: \033[m'))
print('')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converver para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
print('\033[1;35m=>\033[m' * 40)
opção = str(input('sua opção: '))[0]
while opção == '1' or '2' or '3':
    if opção == '1':
        binario = bin(numero)
        print('CONVERTENDO PARA BINÁRIO: ', '\033[1;34m', str(binario[2:]), '\033[m')
        break
    elif opção == '2':
        octal = oct(numero)
        print('CONVERTENDO PARA OCTAL: ', '\033[1;31m', str(octal[2:]), '\033[m')
        break
    elif opção == '3':
        hexadecimal = hex(numero)
        print('CONVERTENDO PARA HEXADECIMAL', '\033[1;32m', str(hexadecimal[2:]), '\033[m')
        break
    else:
        opção = str(input('Opção inválida... Digite um valor entre [1 - 3]'))[0]