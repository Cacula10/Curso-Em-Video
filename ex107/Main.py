from ex107 import moeda

preço = float(input('Digite o preço R$: '))
print(f'A metade de R${preço} é R${moeda.metade(preço)}')
print(f'O dobro de R${preço} é R${moeda.dobro(preço)}')
print(f'Aumentando 10% de R${preço} temos R${moeda.aumentar(preço, taxa=0.10)} ')
print(f'Reduzindo 15% de R${preço} temos R${moeda.diminuir(preço, taxa=0.15)} ')