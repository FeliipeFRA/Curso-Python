'''print('\033[1;31;40m ~= TAL DA P.A. v3.0 FILHO =~ \033[m\n' + '\033[1;31m-\033[m' * 30)
p = int(input("Primeiro Termo: "))
r = int(input("Razão: "))
print('\033[1;31m-\033[m' * 30)
end = False
t = 0
while not end:
    print(f"\033[1;31m{p}", end=' ')
    t += 1
    if t != 10:
        p += r
    if t == 10:
        print("-> PAUSA")
        end = True
nt = 1
while nt != 0:
    print('\033[1;31m-\033[m' * 30)
    nt = int(input("Deseja ver mais quantos termos? "))
    tt = t + nt
    fim = False
    print('\033[1;31m-\033[m' * 30)
    while not fim:
        if nt == 0:
            fim = True
        else:
            p += r
            print(f"\033[1;31m{p}\033[m", end=' ')
            t += 1
            if t == tt:
                print("\033[1;31m-> PAUSA\033[m")
                fim = True
    if nt == 0:
        print(f"\033[1;31mFinalizando sistema com {t} termos mostrados...\033[m")'''
print('\033[1;31;40m ~= TAL DA P.A. v3.0 FILHO =~ \033[m\n' + '\033[1;31m-\033[m' * 30)
p = int(input("Primeiro Termo: "))
r = int(input("Razão: "))
t = 1
tot = 0
mais = 10
while mais != 0:
    tot += mais
    while t <= tot:
        print(f"\033[1;31m{p}", end=' ')
        p += r
        t += 1
    print("-> PAUSA")
    mais = int(input("\033[m- Deseja ver mais quantos termos? "))
print('\033[1;31m-\033[m' * 30)
print(f"{t-1} termos mostrados.\nFinalizando sistema...")
