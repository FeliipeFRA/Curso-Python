jogadores = []
print(f"\033[1;31m=\033[m" * 30)
for i in range(0, 5):
    jogadores.append(str(input("- Adicione um jogador ao time: ")))
for num, j in enumerate(jogadores):
    print(f"- O {num+1}º jogador é o {j}")
print("FIM DO TIME")