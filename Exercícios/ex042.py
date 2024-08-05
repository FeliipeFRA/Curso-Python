print('\033[1;31m•\033[m Insira o tamanho de 3 retas para calcular se é possível formar um '
      'triângulo com elas e qual seu tipo.')
r1 = float(input('\033[1;31mTAMANHO DA RETA 1:\n-----> \033[m'))
r2 = float(input('\033[1;32mTAMANHO DA RETA 1:\n-----> \033[m'))
r3 = float(input('\033[1;33mTAMANHO DA RETA 1:\n-----> \033[m'))
print('\033[1;31m-\033[m' * 35)
if (r2 - r3) < r1 < (r2 + r3) and (r1 - r3) < r2 < (r1 + r3) and (r1 - r2) < r3 < (r1 + r2):
    print('\033[1;32mÉ POSSÍVEL!')
    if r1 == r2 == r3:
        print('\033[1;31m•\033[m\033[1m Triângulo do tipo: \033[m\033[1;31mEQUILÁTERO\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[1;31m•\033[m\033[1m Triângulo do tipo: \033[m\033[1;31mESCALENO\033[m')
    else:
        print('\033[1;31m•\033[m\033[1m Triângulo do tipo: \033[m\033[1;31mISÓSCELES\033[m')
else:
    print('\033[1;31mNÃO É POSSÍVEL!')
