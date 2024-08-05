import math
print('\033[1;31;40m~= SIN, COS E TAN =~\033[m\n' + '\033[1;31m-\033[m' * 20)
ang = float(input('\033[1;31m•\033[m Insira um \033[1;31mÂNGULO\033[m em \033[1;31mGRAUS\033[m:\n\033[1;31m-----> '
                  '\033[m'))
rad = math.radians(ang)
s = math.sin(rad)
c = math.cos(rad)
t = math.tan(rad)
print('\033[1;31m-\033[m' * 20 + f'\nO ângulo de {ang}º possui: \n\033[1;31m•\033[m SENO: '
                                 f'\033[1;4;31m{s:.2f}\033[m\n\033[1;31m•\033[m COSSENO:\033[m '
                                 f'\033[1;4;31m{c:.2f}\033[m\n\033[1;31m•\033[m '
                                 f'TANGENTE: \033[1;4;31m{t:.2f}')
