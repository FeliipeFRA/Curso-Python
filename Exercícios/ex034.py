print('\033[1;31;40m    ~= TAL DO AUMENTO =~    \033[m\n' + '\033[1;31m-\033[m' * 28)
s = int((input('\033[1;31m•\033[m Salário:\n\033[1;32m-----> R$\033[m')))
print('\033[m' + '\033[1;31m-\033[m' * 28)
if s > 1250:
    print(f'\033[1m O aumento será de \033[1;34m10%\033[m\033[1m.\033[m')
    print(f'Após o aumento, seu salário será \033[1;4;33mR${s+(s*0.10):.2f}\033[m.')
else:
    print(f'\033[1mO aumento será de \033[1;34m15%\033[m\033[1m.\033[m')
    print(f'Após o aumento, seu salário será \033[1;4;33mR${s+(s*0.15):.2f}\033[m.')
