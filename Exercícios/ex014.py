print('\033[1;31;40m~~= CONVERSOR DE TEMPERATURAS =~\033[m\n' + '\033[1;31m-\033[m' * 32)
c = float(input('\033[1;31m•\033[m Insira a temperatura em \033[1;32mºC\033[m:\n\033[1;31m----->\033[m '))
f = (c * 9 / 5) + 32
print('\033[1;31m-\033[m' * 32+ f'\n\033[1;32m{c}ºC\033[m é igual a: \033[1;34m{f}ºF')
