def leiaInt():
    while True:
        try:
            num = int(input("- Insira um valor INTEIRO: "))
        except ValueError:
            print("\033[1;31mTipo de dado inválido! Tente novamente.\033[m")
            continue
        except KeyboardInterrupt:
            print(f"{"\033[1;31mO usuário não informou dados\033[m".center(35)}")
            return 0
        else:
            return num


def leiaFloat():
    while True:
        try:
            num = str(input("- Insira um valor REAL: ")).replace(",", ".")
            num = float(num)
        except ValueError:
            print("\033[1;31mTipo de dado inválido! Tente novamente.\033[m")
        except KeyboardInterrupt:
            print(f"{"\033[1;31mO usuário não informou dados\033[m".center(35)}")
            return 0
        else:
            return num
