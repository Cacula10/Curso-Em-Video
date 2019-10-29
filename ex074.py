from random import randint
sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(sorteio)
if sorteio[0] <= sorteio[1] and sorteio[0] <= sorteio[2] and sorteio[0]<= sorteio[3] and sorteio[0] <= sorteio[4] and sorteio[0] <= sorteio[5]:
    print('O menor valor é:',sorteio[0])
