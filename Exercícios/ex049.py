print('\033[1;31;40m ~= TAL DA TABUADA COM FOR =~ \033[m\n' + '\033[1;31m-\033[m' * 30)
num = int(input('\033[1;31m-\033[m \033[1mQuer tabuada de qual número meu fi?\n' + '\033[1;31m----->\033[m '))
print('\033[1;31m-\033[m' * 30)
print(f'\033[1;31;40m      ~= TABUADA DO {num} =~      \033[m')
for i in range(1, 11):
    print(f'\033[1;31m{num}\033[m x \033[1;32m{i}\033[m = \033[1;4;33m{i * num}\033[m')
