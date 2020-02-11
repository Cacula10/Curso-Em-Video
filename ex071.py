print('<>' * 20)
print('{:*^50}'.format('\033[1:31mBANCO DO CAÇULA\033[m'))
print('<>' * 20)
rest100 = 0
saque = int(input('Qual o valor você quer sacar? R$ '))
total = saque
céd = 100
totalcéd = 0

while True:
    if total >= céd:
        total -= céd
        totalcéd += 1
    else:
        if totalcéd > 0:
            print(f'O total {totalcéd} cédulas de {céd} cédulas')
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        totalcéd = 0
        if total == 0:
            break
print('<>' * 20)
print('Volte sempre ao \033[1:31mBANCO DO CAÇULA!\033[m')
print('Tenha um bom dia!')