def notas(* avaliacoes, sit=False):
    """
    :param avaliacoes: Função para avaliar notas e situação de vários alunos
    :param sit: Parametro que aceita uma ou varias notas dos alunos
    :return: Retorna um dicionario com várias informações sobre a situação da Turma
    """
    resp = dict()
    resp['Total'] = len(avaliacoes)
    resp['Maior'] = max(avaliacoes)
    resp['Menor'] = min(avaliacoes)
    resp['Media'] = sum(avaliacoes)/resp['Total']
    if sit:
        if resp['Media'] >= 7:
            resp['Situação'] = 'Boa'
        elif resp['Media'] >= 5:
            resp['Situação'] = 'Razoavel'
        else:
            resp['Situação'] = 'Ruim'
    return resp


# Programa Principal
resp = notas(5, 10, 10, sit=True)
#help(notas)
print(resp)