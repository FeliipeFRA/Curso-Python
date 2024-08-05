print('\033[1;31;40m    ~= TAL DO IMC v1.0 =~    \033[m\n' + '\033[1;31m-\033[m' * 29)
print('\033[1m- Insira seu \033[1;31mPESO\033[m\033[1m e \033[1;31mALTURA\033[m\033[1m para calcular seu '
      '\033[1;31mIMC (Índice de Massa Corporal)\033[m\033[1m.')
peso = float(input('\033[1;31m•\033[m Peso \033[1;31m(Kg)\033[m:\033[1;31m\n-----> \033[m'))
altura = float(input('\033[1;31m•\033[m Altura \033[1;31m(m)\033[m:\033[1;31m\n-----> \033[m'))
print('\033[1;31m-\033[m' * 29)
if peso == 0 or altura == 0:
    print('\033[1m- Peso ou altura \033[1;31mINVÁLIDA\033[m\033[1m! Tente novamente.\033[m')
else:
    imc = peso / (altura ** 2)
    print('\033[1mSeu IMC é:\033[m')
    if imc < 18.5:
        print(f'\033[1;34m{imc:.1f} - ABAIXO DO PESO (!)')
    elif imc < 25:
        print(f'\033[1;32m{imc:.1f} - PESO IDEAL')
    elif imc < 30:
        print(f'\033[1;35m{imc:.1f} - ACIMA DO PESO (!)')
    elif imc < 40:
        print(f'\033[1;33m{imc:.1f} - OBESIDADE (!!)')
    else:
        print(f'\033[1;31m{imc:.1f} - OBESIDADE MÓRBIDA (!!!)')
