from random import choice
alunos = []
for aluno in range(1, 5):
    alunos.append(str(input(f'Informe o nome do {aluno} aluno: ')))

print(choice(alunos))