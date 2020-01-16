# usar o "in" para encontrar algo dentro de uma string (exercicios 24 e 25)
# usar o [:] se quiser achar algo com uma posição especifica
# no exercicio 26 não foi explicado como não calcular os espaços dentro da frase

## posso usar dois ou mais métodos no msm objeto

# Como centralizar um print =======   print('{:=^35}'.format(' Carregando Resultados...')) ==== ex.028.py

# Aula 11 ensina as cores e no exercicio 30,39 também
# \033[0,1,4,7;  30,31,32,33,34,35,36,37;   40,41,42,43,44,45,46,47 e termina com o m
# para finalizar usamos o \033[-m  somente isso

# ex033 ajuda comparar 3 valores
# ex044 Ensina a centralizar texto

# no exericio 45 eu uso o randint e o choice

# Utilizo o strip para eliminar os espaços de antes e depois das frases (evitar erros do usuario)
# Utilizo o split para tirar os espaços do meio da frase e depois o join para juntar tudo desconsiderando os espaços

# para localizar extremos dentro de uma lista, veja exercicio 55 com o laço for (sempre progamar desssa forma e nao fazer gambiarra)

# Estruras de repeticão For e While >>> Usamos a estrutura while pois ela permite encontrar algo quando não sabemos aonde esse algo esta... diferente do for que precisamos colocar um range de 1-10, por exemplo... Quando você nao sabe o limite da sua lista e deseja percorrrer ela, entao usamos o while entao ele percorrre a lista até encontrar (lembrar que precisar conhecer o conteudo da sua lista para fazer o while(enquanto) senao ele pode se perder no meio do caminho)
# estrutra while é quando nao sabemos o limite
# no for eu preciso de um padrao e no while não...no while com ajudar de um if consigo fazer qualquer coisa
# no while aula14 ele usa 3 "if" if tiver chão anda...if tiver buraco pula.. if tiver moeda pega... até chegar na maça
# nao existe mais rapido entre o while e o for
# Exercicioo 056 ajuda a usar o "in" dentro do laço for, ao invez de usar o .upper(), podemos usar o in
# exercicios 65 posso usar p lembrar como faço para achar o menor e maior valor
# do while nao existe em python porem podemos fazer de outra forma
# Eu uso o while True quando eu quiser fazer algo infinito ou até que ele encontre algo e eu uso o break para sair do laço. (aula 15)

""""
COMO CONECTAR NA BASE

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=10.100.188.129\ISAJ01;"
    "Database=SPJUSP;"
    "uid=saj;pwd=nltrecRephlcrA"
)

cursor = conn.cursor()

cursor.execute("SQL")

"""

