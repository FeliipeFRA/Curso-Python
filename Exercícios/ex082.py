numi = []
nump = []
num = []
while True:
    num.append(int(input("\033[1;31m-\033[m Valor a ser adicionado: ")))
    cont = str(input("\033[1;31m-\033[m Deseja continuar? [S/N] ")).upper().strip()[0]
    while cont not in "SN":
        cont = str(input("\033[1;31m-\033[m Deseja continuar? [S/N] ")).upper().strip()[0]
    if cont == "N":
        break
print("\033[1;31m=-" * 20)
for v in range(0, len(num)):
    if num[v] % 2 == 0:
        nump.append(num[v])
    else:
        numi.append(num[v])
print("ANÁLISE DE DADOS".center(40, " "))
print(f"-\033[m Lista original: \n\033[1;31m{num}")
if not nump:
    print("NÃO FORAM ENCONTRADOS VALORES PARES!")
else:
    print(f"-\033[m Lista com valores pares: \n\033[1;31m{nump}")
if not numi:
    print("NÃO FORAM ENCONTRADOS VALORES ÍMPARES!")
else:
    print(f"-\033[m Lista com valores ímpares: \n\033[1;31m{numi}")
