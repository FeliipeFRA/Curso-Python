pessoas = []
dados = []
pes = 0.0
lev = 0.0
print("\033[1;32m       CADASTRO SERMED".center(30, " "))
while True:
    print(("\033[1;32m=" * 30) + "\033[m")
    dados.append(str(input("\033[1;32m-\033[m Nome: ")))
    dados.append(float(input("\033[1;32m-\033[m Peso: ")))
    if len(pessoas) == 0:
        pes = lev = dados[1]
    else:
        if dados[1] <= lev:
            lev = dados[1]
        if dados[1] > pes:
            pes = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    print("\033[1;32mPACIENTE CADASTRADO COM SUCESSO!\033[m")
    print(("\033[1;32m=" * 30) + "\033[m")
    cont = str(input("\033[1;32m-\033[m Deseja continuar? ")).strip().upper()
    while cont != "S" and cont != "N":
        print(f"\033[1;31mOPÇÃO INVÁLIDA!")
        cont = str(input("\033[1;32m-\033[m Deseja continuar? ")).strip().upper()
    if cont == "N":
        print(("\033[1;32m=" * 30) + "\033[m")
        print("\033[1;32mFINALIZANDO CADASTROS...\033[m")
        break
corpulentos = []
esqueleticos = []
for p in range(0, len(pessoas)):
    if pessoas[p][1] == pes:
        corpulentos.append(pessoas[p][0])
    if pessoas[p][1] == lev:
        esqueleticos.append(pessoas[p][0])
print(("\033[1;32m=" * 30) + "\033[m")
print(f"\033[1;32m-\033[m Foram cadastradas \033[1;32m{len(pessoas)} pessoas\033[m.")
print(f"\033[1;32m-\033[m O maior peso registrado foi de \033[1;32m{pes:.2f}KG\033[m. Do(s) paciente(s): "
      f"\033[1;32m{corpulentos}\033[m")
print(f"\033[1;32m-\033[m O menor peso registrado foi de \033[1;32m{lev:.2f}KG\033[m. Do(s) paciente(s): "
      f"\033[1;32m{esqueleticos}\033[m")
