from time import sleep


def maior(* num):
    m = 0
    print('-=' * 20)
    print(f"Analizando os valores:\n\033[1;31m[ ", end='')
    for i, n in enumerate(num):
        if i == 0:
            m = n
        else:
            if n > m:
                m = n
        sleep(1 / 4)
        print(f"{n}", end=" ")
    print("]\033[m")
    print(f"Valor(es) informado(s) no total: \033[1;31m{len(num)}\033[m")
    print(f"Maior valor informado: \033[1;31m{m}\033[m")
    sleep(2)


# main
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
