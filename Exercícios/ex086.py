print("GERADOR DE MATRIZ".center(32, " "))
print("\033[1;31m=" * 32)
matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f"-\033[m Valor para a posição \033[1;31m{l, c}: "))
        matriz[l].append(n)
print("\033[1;31m=" * 32)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]".center(11, " "), end='')
    print()
