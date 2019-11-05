# Se eu quiser verificar se existe algo dentro independente da posicao na string eu uso o "in".
# Nesse caso eu não preciso criar uma outra variavel só para armazenar o valor de T/F

nome = str(input('Qual o seu nome completo ? ')).strip()
print('O seu nome tem silva ? {} '.format('SILVA' in nome.upper()))