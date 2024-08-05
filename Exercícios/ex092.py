from datetime import datetime
print(f"\033[1;31m{'NOVO REGISTRO':^30}\033[m")
print("\033[1;31m=\033[m" * 30)
trabalhador = {}
trabalhador['Nome'] = str(input("- Nome: "))
trabalhador['Idade'] = (datetime.now().year - (int(input("- Ano de Nascimento: "))))
trabalhador['CTPS'] = int(input("- CTPS \033[1;31m[0]\033[m: "))
if trabalhador['CTPS'] > 0:
    trabalhador['Contratação'] = int(input("- Ano de Contratação: "))
    trabalhador['Salário'] = float(input("- Salário: R$"))
    trabalhador['Aposentadoria'] = trabalhador['Idade'] + (35 - (datetime.now().year - trabalhador['Contratação']))
print("\033[1;31m=\033[m" * 30)
print(f"\033[1;31m{'FICHA CADASTRAL':^30}\033[m")
print("\033[1;31m=\033[m" * 30)
for k, v in trabalhador.items():
    if k == 'Aposentadoria' and v <= trabalhador['Idade']:
        print(f"\033[1;31m{k + ':':<20}\033[m{'Aposentado':>10}")
    elif k == 'Idade' or k == 'Aposentadoria':
        print(f"\033[1;31m{k + ':':<20}\033[m",f"{v} anos".rjust(9, ' '))
    elif k == 'Salário':
        print(f"\033[1;31m{k + ':':<20}\033[m",f"R${v:.2f}".rjust(9, ' '))
    else:
        print(f"\033[1;31m{k+':':<20}\033[m{v:>10}")
print("\033[1;31m=\033[m" * 30)