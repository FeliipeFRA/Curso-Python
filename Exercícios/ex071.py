print("\033[1;41m-= BANCO SANTANDER =-\033[m")
print("\033[1;31m-\033[m" * 27)
v = int(input("\033[1;31m-\033[m Valor a ser sacado: R$"))
ced50 = ced20 = ced10 = ced1 = 0
while True:
    if v >= 50:
        v -= 50
        ced50 += 1
    else:
        if v >= 20:
            v -= 20
            ced20 += 1
        else:
            if v >= 10:
                v -= 10
                ced10 += 1
            else:
                if v >= 1:
                    v -= 1
                    ced1 += 1
    if v == 0:
        break
if ced50 > 0:
    print(f"\033[1;31m- {ced50}\033[m cédulas de \033[1;31mR$50\033[m.")
if ced20 > 0:
    print(f"\033[1;31m- {ced20}\033[m cédulas de \033[1;31mR$20\033[m.")
if ced10 > 0:
    print(f"\033[1;31m- {ced10}\033[m cédulas de \033[1;31mR$10\033[m.")
if ced1 > 0:
    print(f"\033[1;31m- {ced1}\033[m cédulas de \033[1;31mR$1\033[m.")
print("\033[1;31m-\033[m" * 27)
