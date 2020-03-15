from ex108 import moeda

preço = float(input('Digite o preço R$: '))
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))} ')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'Aumentando 50% de {moeda.moeda(preço)} o novo preço é {moeda.moeda(moeda.aumentar(preço, 0.50))}')
print(f'Reduzindo 10% de {moeda.moeda(preço)} o novo preço é {moeda.moeda(moeda.diminuir(preço, 0.10))}')