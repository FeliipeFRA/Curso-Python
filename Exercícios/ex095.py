jogadores = []
jogador = {}
g = []
print(f"\033[1;32m{'SOFASCORE':^70}\033[m")
while True:
    tot = 0
    print("\033[1;32m=\033[m" * 70)
    jogador['Nome'] = str(input("\033[1;32m-\033[m Nome do jogador: ")).strip()
    jogador['Camisa'] = int(input("\033[1;32m-\033[m Nº da camisa: "))
    jogador['Time'] = str(input("\033[1;32m-\033[m Time do jogador: ")).upper().strip()
    p = int(input(f"\033[1;32m-\033[m Quantas partidas \033[1;32m{jogador['Nome']}\033[m "
                  f"jogou nessa temporada? "))
    print("\033[1;32m=\033[m" * 70)
    for i in range(0, p):
        gol = (int(input(f"\033[1;32m-\033[m Gols feitos na {i + 1}ª partida: ")))
        tot += gol
        g.append(gol)
    jogador['Gols'] = g[:]
    jogador['Total'] = tot
    jogadores.append(jogador.copy())
    jogador.clear()
    g.clear()
    print("\033[1;32m=\033[m" * 70)
    print("\033[1;32m- JOGADOR CADASTRADO COM SUCESSO!\033[m")
    print("\033[1;32m=\033[m" * 70)
    cont = str(input("\033[1;32m-\033[m Deseja cadastrar mais um jogador? [S/N] ")).upper().strip()[0]
    while cont not in "SN":
        print("\033[1;31mOpção inválida! Tente novamente.\033[m")
        print("\033[1;32m=\033[m" * 70)
        cont = str(input("\033[1;32m-\033[m Deseja cadastrar mais um jogador? [S/N] ")).upper().strip()[0]
    if cont == "N":
        break
print("\033[1;32m=" * 70)
print("CÓD.".ljust(6, " ") + "NOME (CAMISA)".ljust(25, " ") +
      "GOLS".ljust(25, " ") + "TOTAL DE GOLS".ljust(14, " "))
print("\033[1;32m=\033[m" * 70)
for j in range(0, (len(jogadores))):
    print(f"{j}".ljust(6, " ") +
          f"{jogadores[j]['Nome']} ({jogadores[j]['Camisa']})".ljust(25, " ")
          + f"{jogadores[j]['Gols']}".ljust(25, " ")
          + f"{jogadores[j]['Total']}".center(14, " "))
while True:
    print("\033[1;32m=\033[m" * 70)
    cod = int(input("\033[1;32m-\033[m Mostrar dados de qual jogador? \033[1;31m[999 finaliza]\033[m "))
    if cod == 999:
        break
    if cod > (len(jogadores) - 1) or cod < 0:
        print("\033[1;32m=\033[m" * 70)
        print("\033[1;31m Jogador não encontrado! Tente novamente.")
    else:
        print("\033[1;32m=\033[m" * 70)
        print(f"\033[1;32m{'DADOS DO JOGADOR':^70}\033[m")
        print(f"\033[1;32m-\033[m {jogadores[cod]['Nome']}, camisa {jogadores[cod]['Camisa']}, "
              f"pelo \033[1;32m{jogadores[cod]['Time']}\033[m nessa temporada:")
        for i in range(0, len(jogadores[cod]['Gols'])):
            print(f"\033[1;32m Na {i + 1}ª partida fez {jogadores[cod]['Gols'][i]} gols\033[m")
        print("\033[1;32m=\033[m" * 70)
        print(f"\033[1;32m-\033[m Total de gols: {jogadores[cod]['Total']}")
        print(f"\033[1;32m-\033[m Média de gols: {jogadores[cod]['Total'] / len(jogadores[cod]['Gols']):.2f} por partida")
print("\033[1;32m=\033[m" * 70)
print("\033[1;32mFINALIZANDO SISTEMA...\033[m")
