num = int(input("Digite um numero: "))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
raiz2 = pow(num, (1/2))

print('O dobro de {} vale {}'.format(num, dobro))
print('O triplo de {} vale {}'.format(num, triplo))
print('A raiz quadrada de {} vale {:.2f}'.format(num, raiz))
print('A segunda opção de calcular a raiz quadrada do numero {} é:  {:.2f}'.format(num, raiz2))