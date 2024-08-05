print('\033[1;31;40m~= CALCULANDO DESCONTOS =~\033[m\n' + '\033[1;31m-\033[m' * 26)
n = str(input('\033[1;31m•\033[m Insira o nome do produto:\n\033[1;31m-----> \033[m'))
p = float(input('\033[1;31m•\033[m Insira o preco do produto:\n\033[1;32m-----> R$\033[m'))
np = p - (p * 5 / 100)
print(f'O produto \033[1;31m"{n}"\033[m custava \033[1;32mR${p:.2f}\033[m'
      f'. Com o desconto de \033[1;33m5%\033[m custa: \033[1;33mR${np:.2f}')
