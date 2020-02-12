print('=>' * 15)
print('{:-^30}'.format('EXERCICIO 072'))
print('=>' * 15)
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um numero entre 0 e 20: '))
while numero > 20 or numero < 0:
    numero = int(input('Erro... Favor digitar um numero entre 0 e 20: '))
print(f'O número que você digitou foi: {tupla[numero]}')