print('\033[1;31;40m~= CONVERSOR DE MOEDAS =~\033[m\n' + '\033[1;31m-\033[m' * 25)
s = float(input('\033[1;31m•\033[m Saldo atual:\n\033[1;32m-----> R$\033[m'))
cot_d = 4.91
cot_e = 5.39
d = s / cot_d
e = s / cot_e
print(('\033[1;31m-\033[m' * 25) + f'\nCom \033[1;32mR${s:.2f}\033[m, é possível comprar \033[1;34mU${d:.2f}\033[m ou \033[1;33m€{e:.2f}.')
