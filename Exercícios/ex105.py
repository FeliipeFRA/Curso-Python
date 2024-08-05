def notas(*n, sit=False):
    """
    -> Função que recebe notas de alunos e analisa.
    :param n:  Uma ou mais notas
    :param sit: Opcional, exibe a situação da sala de acordo com a média.
    :return: Dicionário com as informações sobre a turma.
    """
    sala = dict()
    sala['Total'] = len(n)
    sala['Menor'] = min(n)
    sala['Maior'] = max(n)
    sala['Média'] = sum(n)/len(n)
    if sit:
        if sala['Média'] <= 5:
            sala['Situação'] = "Ruim"
        elif sala['Média'] <= 7:
            sala['Situação'] = "Razoável"
        else:
            sala['Situação'] = "Boa"
    return sala


# main
nonoA = notas(5.5, 2.5, 8.5, sit=True)
print(nonoA)
