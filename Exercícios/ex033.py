print('\033[1;31;40m    ~= TAL DO MAIOR E MENOR =~    \033[m\n' + '\033[1;31m-\033[m' * 34)
n1 = int(input('\033[1;31m• VALOR 1:\033[m '))
n2 = int(input('\033[1;32m• VALOR 2:\033[m '))
n3 = int(input('\033[1;33m• VALOR 3:\033[m '))
if n1 > n2:
    if n1 > n3:
        if n3 > n2:
            print(f'O \033[1;35mMAIOR\033[m número é o \033[1;31m{n1}\033[m e o \033[1;35mMENOR\033[m número é o \033[1;32m{n2}\033[m.')
        else:
            print(f'O \033[1;35mMAIOR\033[m número é o \033[1;31m{n1}\033[m e o \033[1;35mMENOR\033[m número é o \033[1;33m{n3}\033[m.')
    else:
        print(f'O \033[1;35mMAIOR\033[m número é o \033[1;33m{n3}\033[m e o \033[1;35mMENOR\033[m número é o \033[1;32m{n2}\033[m.')
else:
    if n2 > n3:
        if n3 > n1:
            print(f'O \033[1;35mMAIOR\033[m número é o \033[1;32m{n2}\033[m e o \033[1;35mMENOR\033[m número é o \033[1;31m{n1}\033[m.')
        else:
            print(f'O \033[1;35mMAIOR\033[m número é o \033[1;32m{n2}\033[m e o \033[1;35mMENOR\033[m número é o \033[1;33m{n3}\033[m.')
    else:
        print(f'O \033[1;35mMAIOR\033[m número é o \033[1;33m{n3}\033[m e o \033[1;35mMENOR\033[m número é o \033[1;31m{n1}\033[m.')
