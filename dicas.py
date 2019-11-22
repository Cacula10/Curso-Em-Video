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