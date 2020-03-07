from random import randint
randint(1, 10)
lista = list()
listapares = list()


def sorteio(num):
    for v in range(1, num+1):
        lista.append(randint(1, 10))

def pares():
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    return soma

# Programa principal

sorteio(4)
print(f'Sorteando {len(lista)} valores da lista: {lista}')
print(f'Somando os valores pares da lista {lista}, temos o resultado {pares()}')