print('\033[1;31;40m ~= TAL DA P.A. FILHO =~ \033[m\n' + '\033[1;31m-\033[m' * 25)
a = int(input('\033[1;31m-\033[m \033[1;31mPrimeiro termo\033[m da '
              '\033[1;33mProgressão Aritmética\033[m:\n\033[1;31m-----> \033[m'))
r = int(input('\033[1;31m-\033[m \033[1;31mRazão\033[m da '
              '\033[1;33mProgressão Aritmética\033[m:\n\033[1;31m-----> \033[m'))
print('\033[1;31m-\033[m' * 25)
pa = 0
for i in range(1, 11):
    if i != 1:
        a += r
    print(f'\033[1;31m-\033[m {i}º termo: \033[1;33m{a}\033[m')
