print('\033[1;31;40m~= TAL DOS DIGÍTOS =~\033[m\n' + '\033[1;31m-\033[m' * 21)
num = (input('\033[1;31m•\033[m Digite um número entre 0 e 9999: \n\033[1;31m-----> \033[m'))
numdiv = list(num)
if len(num) == 4:
    print(f'''\033[1;31m•\033[m Número escolhido: \033[1;4;40m{num}\033[m
\033[1;31m•\033[m Unidade: \033[1;4;31m{num[3]}\033[m
\033[1;32m•\033[m Dezena: \033[1;4;32m{num[2]}\033[m
\033[1;33m•\033[m Centena: \033[1;4;33m{num[1]}\033[m
\033[1;34m•\033[m Milhar: \033[1;4;34m{num[0]}\033[m''')
elif len(num) == 3:
    print(f'''\033[1;31m•\033[m Número escolhido: \033[1;4;40m{num}\033[m
\033[1;31m•\033[m Unidade: \033[1;4;31m{num[2]}\033[m
\033[1;32m•\033[m Dezena: \033[1;4;32m{num[1]}\033[m
\033[1;33m•\033[m Centena: \033[1;4;33m{num[0]}\033[m''')
elif len(num) == 2:
    print(f'''\033[1;31m•\033[m Número escolhido: \033[1;4;40m{num}\033[m
\033[1;31m•\033[m Unidade: \033[1;4;31m{num[1]}\033[m
\033[1;32m•\033[m Dezena: \033[1;4;32m{num[0]}\033[m''')
elif len(num) == 1:
    print(f'''\033[1;31m•\033[m Número escolhido: \033[1;4;40m{num}\033[m
\033[1;31m•\033[m Unidade: \033[1;4;31m{num[0]}\033[m''')
elif num == '':
    print('\033[1;31m\nVocê precisa digitar algum valor FILHO DA PUTA!')
else:
    print('\033[1;31m\nO número digitado é maior que 9999, tente outro valor.')
