print('\033[1;31;40m~= P\033[1;32mI\033[m\033[1;33;40mN\033[m\033[1;34;40mT\033[m\033[1;35;40mA\033[m\033[1;36;40mN\033'
      '[m\033[1;37;40mD\033[m\033[1;31;40mO \033[1;32mP\033[m\033[1;33;40mA\033[m\033[1;34;40mR'
      '\033[1;35;40mE\033[m\033[1;36;40mD\033[m\033[1;37;40mE\033[m'
      '\033[1;31;40m =~\033[m\n'
      + '\033[1;31m-\033[m' * 21)
larg = float(input('\033[1;31m•\033[m \033[1;33mLARGURA\033[m da parede em \033[1;33mMETROS\033[m:\n'
                   '\033[1;31m----->\033[m '))
alt = float(input('\033[1;31m•\033[m \033[1;32mALTURA\033[m da parede em \033[1;32mMETROS\033[m:\n'
                  '\033[1;31m----->\033[m '))
a = alt * larg
print('\033[1;31m-\033[m' * 21 + f'\nA parede tem uma dimensão de \033[1;33m{larg}\033[m x \033[1;32m{alt}\033[m '
                                 f'e possui uma área de \033[1;31m{a}m²\033[m.')
print(f'Portanto, será(ão) necessário(s) \033[1;35m{a / 2} litro(s)\033[m de tinta para pinta-lá.')
