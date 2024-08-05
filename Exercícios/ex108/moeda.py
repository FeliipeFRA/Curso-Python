def moeda(valor=0, moeda='R$'):
    return f"{moeda}{valor:.2f}".replace(".",",")


def aumentar(valor=0, pctg=0):
    valor += (pctg/100) * valor
    return valor


def diminuir(valor=0, pctg=0):
    valor -= (pctg/100) * valor
    return valor


def dobro(valor=0):
    valor *= 2
    return valor


def metade(valor=0):
    valor /= 2
    return valor
