from time import sleep

c = ('\033[m',      # 0 - Sem cor
     '\033[1;41m',  # 1 - Red
     '\033[1;42m',  # 2 - Green
     '\033[1;43m',  # 3 - Yellow
     '\033[1;44m',  # 4 - Blue
     '\033[1;45m')  # 5 - Purple


def pyhelp(fun):
    title(f"Acessando o manual do comando '{fun}'...", 5)
    sleep(1)
    print("\033[1;32m")
    help(fun)
    print("\033[m", end="")
    sleep(3)


def title(texto, cor=0):
    print(f"{c[cor]}-\033[m" * 60)
    print((f"{c[cor]} \033[m" * (((60 - len(texto)) // 2) + len(texto) % 2)), end='')
    print(f"{c[cor]}{texto}\033[m", end='')
    print((f"{c[cor]} \033[m" * ((60 - len(texto)) // 2)))
    print(f"{c[cor]}-{c[0]}" * 60)
    sleep(1/2)


# main
while True:
    title("-= SISTEMA DE AJUDA PyHELP =-", 2)
    funcao = str(input("\033[1;32m-\033[m Função ou Biblioteca \033[1;32m--->\033[m ")).strip().lower()
    if funcao == "fim":
        break
    pyhelp(funcao)


title("FINALIZANDO SISTEMA...", 1)
