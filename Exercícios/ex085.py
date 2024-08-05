numeros = [[], []]
for i in range(0, 7):
    num = int(input(f"\033[1;31m-\033[m Digite o \033[1;31m{i+1}º\033[m valor: "))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print("\033[1;31m=" * 25)
print(f"\033[1;31m-\033[m Lista dos \033[1;31mPARES\033[m: \033[1;31m{sorted(numeros[0])}")
print(f"\033[1;31m-\033[m Lista dos \033[1;31mÍMPARES\033[m: \033[1;31m{sorted(numeros[1])}")
