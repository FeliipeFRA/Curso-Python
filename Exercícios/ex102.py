def fatorial(numero, show=False):
    """
    :param numero: Numero a ser fatorado.
    :param show: (Opcional) Mostra ou não o processo.
    :return: O valor do Fatorial do numero escolhido.
    """
    fat = 1
    for i in range(numero, 0, -1):
        fat *= i
    if show:
        print(f"{numero}", end=' ')
        for i in range(numero - 1, 0, -1):
            print(f"x {i}", end=' ')
        print("=", end=' ')
        return fat
    else:
        return fat


# main
num = int(input("- Número a ser fatorado: "))
op = str(input("- Deseja mostrar o processo de cálculo? [S/N] ")).upper().strip()[0]
while op not in "SN":
    print("Opção inválida! Responda apenas 'S' ou 'N'.")
    op = str(input("- Deseja mostrar o processo de cálculo? [S/N] ")).upper().strip()[0]
print("-" * 45)
if op == "S":
    print(fatorial(num, True))
else:
    print(fatorial(num))
