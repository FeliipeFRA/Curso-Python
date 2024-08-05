def resumo(valor=0, aumpctg=0, redpctg =0):
    print(("-" * 35 + "\n"), f"{"RESUMO DO VALOR":^35}", ("\n" + "-" * 35))
    print(f"{"Valor analisado:":<23} {moeda(valor)}")
    print(f"{"Dobro do valor:":<23} {dobro(valor, True)}")
    print(f"{"Metade do valor:":<23} {metade(valor, True)}")
    print(f"{f"{aumpctg}% de aumento:":<23} {aumentar(valor, aumpctg, True)}")
    print(f"{f"{redpctg}% de redução:":<23} {diminuir(valor, redpctg, True)}")
    print("-" * 35)


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
