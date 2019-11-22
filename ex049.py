print('{:=^50}'.format(' \033[1;34mSISTEMA DA CALCULADORA\033[m '))
print('')
tabuada = int(input('Digite um número para ver a sua tabuada: '))
for v in range(1, 11):
    print(tabuada, 'X', v,  '=  {}'.format(tabuada * v))