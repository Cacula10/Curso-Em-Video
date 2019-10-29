v = input('Digite algo: ')
print('O tipo primitivo desse valor é: {}'.format(type(v)))
print('Só tem espaços: ', v.isspace())# Ele procura se só tem espaço no que for digitado
print('É um numero? ', v.isnumeric())
print('É alfabético ? ', v.isalpha())
print('É alfanumerico ? ', v.isalnum())
print('Está em maiscula? ', v.isupper())
print('Está em mínuscula? ', v.islower())
print('Está em capitalize ?', v.istitle())