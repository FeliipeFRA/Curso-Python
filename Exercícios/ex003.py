print('\033[1;31;40m-~ SOMADOR DE NÚMEROS ~-\033[m\n' + '\033[1;31m-\033[m' * 24)
n1 = int(input('Digite o \033[1;31mvalor 1\033[m: '))
n2 = int(input('Digite o \033[1;32mvalor 2\033[m: '))
soma = n1 + n2
print('-' * 24 + f'\nA soma entre \033[1;31m{n1}\033[m e \033[1;32m{n2}\033[m resulta em: \033[1;4;33m{soma}\033[m!')
