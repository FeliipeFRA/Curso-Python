from datetime import date
print('\033[1;31;40m    ~= TAL DO BISSEXTO FILHO =~    \033[m\n' + '\033[1;31m-\033[m' * 35)
ano = int(input('\033[1;31m•\033[m ANO ESCOLHIDO:    \033[1;31m(0 = Ano atual)\033[m \n\033[1;31m-----> \033[m'))
if ano == 0:
    ano = date.today().year
if (ano % 4) == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano \033[1;33m{ano}\033[m \033[1;32mÉ\033[m um ano \033[1;33mbissexto\033[m.')
else:
    print(f'O ano \033[1;33m{ano}\033[m \033[1;31mNÃO\033[m é \033[1;33mbissexto\033[m.')
