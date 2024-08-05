def aumentar(valor, pctg):
    valor += (pctg/100) * valor
    return valor


def diminuir(valor, pctg):
    valor -= (pctg/100) * valor
    return valor


def dobro(valor):
    valor *= 2
    return valor


def metade(valor):
    valor /= 2
    return valor
