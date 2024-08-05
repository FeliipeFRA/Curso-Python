valores = list()
v = 0
while True:
    print("=" * 30)
    v = (int(input("- Insira um valor: ")))
    if v in valores:
        print("\033[1;31mVALOR JÁ CADASTRADO! Tente outro.\033[m")
    else:
        print("\033[1;32mVALOR ADICIONADO COM SUCESSO!\033[m")
        valores.append(v)
    cont = str(input("- Deseja continuar? [S/N] ")).upper()[0]
    while cont not in "SN":
        print("\033[1;31mOPÇÃO INVÁLIDA! Tente novamente.\033[m")
        cont = str(input("- Deseja continuar? [S/N] ")).upper()[0]
    if cont == "N":
        break
print("=" * 30)
print("- Valores em Ordem Crescente: \033[1;31m")
print(f"{sorted(valores)}".center(30, ' '))
