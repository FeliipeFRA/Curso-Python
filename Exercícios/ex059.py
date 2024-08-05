from time import sleep
print("\033[1;32;40m ~= TAL DA CALCULADORA FILHO =~ \033[m")
v1 = int(input("\033[1;32m-\033[m Valor 1: "))
v2 = int(input("\033[1;32m-\033[m Valor 2: "))
end = False
while not end:
    print("\033[1;32;40m             MENU               \033[m")
    print("\033[1;32m[1]\033[m - Somar")
    print("\033[1;32m[2]\033[m - Multiplicar")
    print("\033[1;32m[3]\033[m - Verificar maior")
    print("\033[1;32m[4]\033[m - Novos valores")
    print("\033[1;32m[5]\033[m - Sair do programa")
    op = int(input("\033[1;32m-----> \033[m"))
    if op == 1:
        print("\033[1;32;40m           RESULTADO:           \033[m ")
        print(f"\033[1;32m- {v1}\033[m mais \033[1;32m{v2}\033[m resulta em \033[1;32m{v1 + v2}\033[m.")
    elif op == 2:
        print("\033[1;32;40m           RESULTADO:           \033[m ")
        print(f"\033[1;32m- {v1}\033[m vezes \033[1;32m{v2}\033[m é \033[1;32m{v1 * v2}\033[m.")
    elif op == 3:
        print("\033[1;32;40m           RESULTADO:           \033[m ")
        if v1 > v2:
            print(f"\033[1;32m-\033[m O maior número entre \033[1;32m{v1}\033[m e \033[1;32m{v2}\033[m é "
                  f"\033[1;32m{v1}\033[m.")
        elif v2 > v1:
            print(f"\033[1;32m-\033[m O maior número entre \033[1;32m{v1}\033[m e \033[1;32m{v2}\033[m é "
                  f"\033[1;32m{v2}\033[m.")
        else:
            print(f"\033[1;32m-\033[m Os valores são \033[1;32mIGUAIS\033[m.")
    elif op == 4:
        print("\033[1;32;40m         NOVOS VALORES:         \033[m ")
        v1 = int(input("\033[1;32m-\033[m Valor 1: "))
        v2 = int(input("\033[1;32m-\033[m Valor 2: "))
    elif op == 5:
        print("\033[1;32;40m   ENCERRANDO CALCULADORA...    \033[m")
        end = True
    else:
        print("\033[1;32;40m         OPÇÃO INVÁLIDA!        \033[m ")
        print(f"\033[1;32m- \033[m Tente novamente.")
    sleep(2)
