def voto(nascimento):
    from datetime import datetime
    idade = datetime.now().year - nascimento
    print('*' * 35)
    if idade < 16:
        return (f'Com {idade} anos: NEGADO votar')
    elif 16 <= idade < 18 or idade > 60:
        return (f'Com {idade} anos: OPCIONAL votar')
    else:
        return (f'Com {idade} anos: OBRIGATÓRIO votar')

print('*' * 35)
ano = int(input('Em que ano você nasceu ? '))
print(voto(ano))
