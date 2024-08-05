print("GERADOR DE MATRIZ".center(32, " "))
print("\033[1;31m=" * 32)
matriz = [[], [], []]
somap = soma3c = maior2l = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f"-\033[m Valor para a posição \033[1;31m{l, c}: "))
        matriz[l].append(n)
print("\033[1;31m=" * 32)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]".center(11, " "), end='')
    print()
print("\033[1;31m=" * 32)
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        if c == 2:
            soma3c += matriz[l][c]
        if l == 1:
            if c == 0:
                maior2l = matriz[l][c]
            else:
                if matriz[l][c] > maior2l:
                    maior2l = matriz[l][c]
print("ANÁLISE DE DADOS".center(32, " "))
print(f"\033[1;31m-\033[m A soma de todos os valores pares digitados é: \033[1;31m{somap}\033[m")
print(f"\033[1;31m-\033[m A soma dos valores da terceira coluna é: \033[1;31m{soma3c}\033[m")
print(f"\033[1;31m-\033[m O maior valor da segunda linha é: \033[1;31m{maior2l}\033[m")