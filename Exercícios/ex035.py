print('\033[1;31;40m    ~= TAL DO TRIÂNGULO v1.0 =~    \033[m\n' + '\033[1;31m-\033[m' * 35)
print('\033[1;31m•\033[m Insira o tamanho de 3 retas para calcular se é possível formar um triângulo com elas.')
r1 = float(input('\033[1;31mTAMANHO DA RETA 1:\n-----> \033[m'))
r2 = float(input('\033[1;32mTAMANHO DA RETA 1:\n-----> \033[m'))
r3 = float(input('\033[1;33mTAMANHO DA RETA 1:\n-----> \033[m'))
print('\033[1;31m-\033[m' * 35)
if (r2 - r3) < r1 < (r2 + r3):
    if (r1 - r3) < r2 < (r1 + r3):
        if (r1 - r2) < r3 < (r1 + r2):
            print('\033[1;32mÉ POSSÍVEL!')
        else:
            print('\033[1;31mNÃO É POSSÍVEL!')
    else:
        print('\033[1;31mNÃO É POSSÍVEL!')
else:
    print('\033[1;31mNÃO É POSSÍVEL!')
