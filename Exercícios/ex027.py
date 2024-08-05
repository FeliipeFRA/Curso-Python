print('\033[1;31;40m  ~= TAL DOS NOMES =~  \033[m\n' + '\033[1;31m-\033[m' * 23)
nome = str(input('\033[1;31m•\033[m Digite seu nome completo: \n\033[1;31m-----> \033[m')).strip()
print(f'\033[1;31m•\033[m Primeiro nome: \033[1;4;31m{nome.split()[0]}\033[m')
print(f'\033[1;31m•\033[m Último nome: \033[1;4;31m{nome.split()[len(nome.split())-1]}\033[m')
