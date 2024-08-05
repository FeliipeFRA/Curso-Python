print('\033[1;31;40m    ~= TAL DO PAR OU ÍMPAR =~    \033[m\n' + '\033[1;31m-\033[m' * 31)
n = int(input('\033[1;31m•\033[m NÚMERO ESCOLHIDO: \n\033[1;31m-----> \033[m'))
nc = f'\033[1;31m{n}\033[m'
print('\033[m' + '\033[1;31m-\033[m' * 31)
if (n % 2) == 0:
    print(f'O número {nc} é \033[1;33mPAR\033[m!')
else:
    print(f'O número {nc} é \033[1;33mÍMPAR\033[m!')
