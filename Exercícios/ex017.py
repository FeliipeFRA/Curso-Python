from math import hypot
print('\033[1;31;40m~= CATETOS E HIPOTENUSA =~\033[m\n' + '\033[1;31m-\033[m' * 26)
cat_o = float(input('\033[1;31m•\033[m Insira o comprimento do \033[1;32mCATETO OPOSTO\033[m em '
                    '\033[1;33mmetros\033[m:\n\033[1;33m----->\033[m '))
cat_a = float(input('\033[1;31m•\033[m Insira o comprimento do \033[1;34mCATETO ADJACENTE\033[m em '
                    '\033[1;33mmetros\033[m:\n\033[1;33m----->\033[m '))
hip = hypot(cat_o, cat_a)
print('\033[1;31m-\033[m' * 26 + f'\nA\033[1;35m HIPOTENUSA\033[m possui\033[1;33m {hip:.2f} '
                                 f'metros\033[m de comprimento.')
