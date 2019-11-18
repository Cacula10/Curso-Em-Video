from time import sleep
from datetime import date
ano_atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - nascimento
sexo = str(input('Informe o seu sexo: [M/F]'))[0].upper()
print('\033[1;34mFAZENDO OS CALCULOS...\033[m')
sleep(2)
print('*' * 70)
if sexo == 'M':
    print('Quem nasceu em \033[1;33m{}\033[m tem \033[1;33m{}\033[m anos em \033[1;33m{}\033[m'.format(nascimento, idade, ano_atual))
    if idade < 18:
        print('Ainda faltam \033[1;34m{}\033[m anos para o alistamento, calma aí JOVEM..\nSeu alistamento será em \033[1;34m{}\033[m'.format(18 - idade, nascimento + 18))
    elif idade == 18:
        print('Maluco ! Quem nasceu em \033[1;35m{}\033[m já tem \033[1;35m{}\033[m anos e precisa se alistar IMEDIATAMENTE.'.format(nascimento, idade))
    else:
        print('Já passou o tempo de alistamento há \033[1;36m{}\033[m anos.\nSeu alistamento foi em \033[1;36m{}\033[m'.format(idade - 18, nascimento + 18))
else:
    print('{:^70}'.format('\033[1;34mO alistamento é apenas para o sexo Masculino\033[m'))
print('*' * 70)