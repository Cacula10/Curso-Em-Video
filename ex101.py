def voto(nasc):
    from datetime import date
    ano = date.today().year
    print('=>' * 15)
    idade = ano - nasc
    if idade <= 17:
        return f'Com {idade} anos. Não vota !'
    elif 16 <= idade < 18 or idade > 65:
        return 'O voto é opcional'
    else:
        return 'O voto é obrigatório !'


# Programa Principal
nasc = int(input('Em que ano você nasceu ? '))
print(voto(nasc))
