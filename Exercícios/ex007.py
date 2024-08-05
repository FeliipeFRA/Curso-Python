print('\033[1;31;40m~= MÉDIA ARITMÉTICA =~\033[m\n' + '\033[1;31m-\033[m' * 22)
n1 = float(input('\033[1;31m•\033[m Insira a \033[1;31mNOTA 1\033[m:\n\033[1;31m-----> \033[m'))
n2 = float(input('\033[1;31m•\033[m Insira a \033[1;32mNOTA 2\033[m:\n\033[1;31m-----> \033[m'))
m = (n1 + n2) / 2
print('\033[1;31m-\033[m' * 22 + f'\nSua \033[1;33mMÉDIA\033[m é: \033[1;4;33m{m:.1f}\033[m')
