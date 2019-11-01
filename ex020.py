import random
alunos = []
for aluno in range(1, 5):
    alunos.append(str(input(f'Informe o {aluno} nome do aluno: ')))

random.shuffle(alunos)
print(alunos)