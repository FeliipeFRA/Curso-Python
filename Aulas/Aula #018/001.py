time = [['Gerson', 20],['Gabigol', 10],
        ['Arrascaeta', 14],['Cebolinha', 11], ['Bruno Henrique', 27]]
jogador = []
print(f"\033[1;31mJOGADOR:".ljust(25, " "), "Nº: \033[m")
for j in time:
    print(f"{j[0]}".ljust(18, " "), f"{j[1]}")
print("\033[1;31m=" * 25)
print(f"\033[1;31m- Contrate um jogador!\033[m")
jogador.append(str(input("NOME DO JOGADOR: ")))
jogador.append(int(input("Nº DA CAMISA: ")))
time.append(jogador[:])
print(f"\033[1;31mJOGADOR:".ljust(25, " "), "Nº: \033[m")
for j in time:
    if j[1] == 10:
        print(f"{j[0]}".ljust(18, " "), f"{j[1]}")