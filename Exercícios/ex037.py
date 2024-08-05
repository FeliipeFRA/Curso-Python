print('\033[1;31;40m    ~= TAL DO RICARDO =~    \033[m\n' + '\033[1;31m-\033[m' * 28)
print('\033[1;31m  -~ CONVERSOR DE BASES ~-  \033[m\n' + '\033[1;31m-\033[m' * 28)
num = int(input('\033[1mNúmero a ser convertido:\n\033[1;31m----->\033[m '))
print('\033[1;31m•\033[m \033[1mAgora escolha a base a ser convertida:\n\033[1;32m- [1] BINÁRIO\033[m\n'
      '\033[1;33m- [2] OCTAL\033[m\n\033[1;34m- [3] HEXADECIMAL\033[m')
base = int(input('\033[1;31m----->\033[m '))
print('\033[1;31m-\033[m' * 28)
print('\033[1;31m•\033[m \033[1mNúmero convertido:\033[m')
if base == 1:
    print(f'{bin(num)[2:]}')
elif base == 2:
    print(f'{oct(num)[2:]}')
elif base == 3:
    print(f'{hex(num)[2:]}')
else:
    print('\033[1mOPÇÃO DE BASE INVÁLIDA!')
