jogador = dict()
flamengo = list()
for j in range(0, 2):
    jogador['Nome'] = str(input("- Nome do jogador: "))
    jogador['Camisa'] = int(input("- Nº da camisa: "))
    jogador['Posicao'] = str(input("- Posição do jogador: "))
    flamengo.append(jogador.copy())
    print("=" * 30)
for j in flamengo:
    for k, v in j.items():
        print(f"{k}: {v}")
    print("=" * 30)
