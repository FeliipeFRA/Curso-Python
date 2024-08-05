print('\033[1;34;40m   ~= SEQUÊNCIA DE FIBONACCI =~   \033[m\n' + '\033[1;34m-\033[m' * 34)
e = int(input("""- Quantos elementos da \033[1;34mSequência 
de Fibonacci\033[m você deseja ver?
\033[1;34m-----> \033[m"""))
print('\033[1;34m-\033[m' * 34)
p = 0
s = 1
c = 0
while c != e:
    if c % 2 == 0:
        print(f"\033[1;34m{p}", end=' ➜ ')
        p += s
    else:
        print(f"\033[1;34m{s}", end=' ➜ ')
        s += p
    c += 1
print("\033[1;34mFIM\033[m")