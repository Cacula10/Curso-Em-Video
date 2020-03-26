from ex109 import moeda

preço = float(input('Digite o preço R$: '))
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço)} ')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f'Aumentando 50% o novo preço é {moeda.aumentar(preço, 0.50, True)}')
print(f'Reduzindo 10%  o novo preço é {moeda.diminuir(preço, 0.10, True)}')
