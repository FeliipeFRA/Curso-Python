cont = soma = 0
while True:
    num = int(input("- Insira um valor \033[1;31m[999]\033[m: "))
    if num == 999:
        break
    cont += 1
    soma += num
print("\033[1;31m-\033[m" * 40)
print(f"A soma dos {cont} valores inseridos resulta em: {soma}")
