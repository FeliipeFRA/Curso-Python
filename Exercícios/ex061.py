print('\033[1;31;40m ~= TAL DA P.A. v2.0 FILHO =~ \033[m\n' + '\033[1;31m-\033[m' * 30)
p = int(input("Primeiro Termo: "))
r = int(input("Razão: "))
print('\033[1;31m-\033[m' * 30)
end = False
t = 0
while not end:
    print(f"\033[1;31m{p}", end=' ')
    p += r
    t += 1
    if t == 10:
        print("-> FIM")
        end = True
