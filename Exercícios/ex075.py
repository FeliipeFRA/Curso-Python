val = (int(input(f"- Valor 1: ")), int(input(f"- Valor 2: ")), int(input(f"- Valor 3: ")), int(input(f"- Valor 4: ")))
cont9 = prim3 = 0
for n in range(0, len(val)):
    if val[n] == 9:
        cont9 += 1
    if val[n] == 3 and prim3 == 0:
        prim3 = n
print(f"- Você digitou os valores: \033[1;31m{val}\033[m")
print(f"- Existem {cont9} valores \033[1;31m'9'\033[m na tupla.")
if prim3 == 0:
    print(f"- Não foi digitado nenhum valor \033[1;31m'3'\033[m.")
else:
    print(f"- O primeiro \033[1;31m'3'\033[m está na {prim3 + 1}ª posição.")
print(f"- Valores pares digitados:", end=" ")
for n in range(0, len(val)):
    if val[n] % 2 == 0:
        print(f"\033[1;31m{val[n]}", end=" ")
