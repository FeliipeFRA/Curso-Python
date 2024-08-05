def moeda(valor=0, currency='R$'):
    return f"{currency}{valor:.2f}".replace(".", ",")


def aumentar(valor=0, pctg=0, formatar=False):
    valor += (pctg/100) * valor
    if formatar:
        return moeda(valor)
    else:
        return valor


def diminuir(valor=0, pctg=0, formatar=False):
    valor -= (pctg/100) * valor
    if formatar:
        return moeda(valor)
    else:
        return valor


def dobro(valor=0, formatar=False):
    valor *= 2
    if formatar:
        return moeda(valor)
    else:
        return valor


def metade(valor=0, formatar=False):
    valor /= 2
    if formatar:
        return moeda(valor)
    else:
        return valor
