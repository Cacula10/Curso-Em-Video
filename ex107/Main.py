from ex107 import moeda

preço = float(input('Digite o preço R$: '))
print(f'A metade de {preço} é {moeda.metade(preço)}')
print(f'O dobro de {preço} é {moeda.dobro(preço)}')
print(f'Aumentando 10% de {preço} temos {moeda.aumentar(preço, taxa=0.10)}')
print(f'Reduzindo 15% de {preço} temos {moeda.diminuir(preço, taxa=0.15)}')