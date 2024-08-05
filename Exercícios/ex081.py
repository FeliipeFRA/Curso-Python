nums = []
while True:
    nums.append(int(input("- Número que deseja adicionar: ")))
    cont = str(input("- Deseja continuar? [S/N] ")).upper().strip()[0]
    while cont not in "SN":
        print("\033[1;31mOPÇÃO INVÁLIDA! Tente novamente.\033[m")
        cont = str(input("- Deseja continuar? [S/N] ")).upper().strip()[0]
    if cont == "N":
        break
print("\033[1;31m=" * 35)
print("LISTA EM ORDEM DECRESCENTE:".center(35, " "))
print(f"{sorted(nums, reverse=True)}".center(35, " "))
print(f"-\033[m Quantidade de números digitados: \033[1;31m{len(nums)}\033[m")
if 5 not in nums:
    print(f"\033[1;31m-\033[m O \033[1;31mnúmero 5 NÃO\033[m está na lista.")
else:
    print(f"\033[1;31m-\033[m O \033[1;31mnúmero 5\033[m \033[1;32mESTÁ\033[m na lista.")
