def voto(ano):
    from datetime import datetime
    i = (datetime.now().year - ano)
    if 65 > i >= 18:
        return ("=" * 30) + f"\nCom {i} anos: VOTO OBRIGATÓRIO"
    if 16 <= i < 18 or i > 65:
        return ("=" * 30) + f"\nCom {i} anos: VOTO OPCIONAL"
    else:
        return ("=" * 30) + f"\nCom {i} anos: NÃO VOTA"


# main

ano = (int(input("- Ano de Nascimento: ")))
print(f"{voto(ano)}")
