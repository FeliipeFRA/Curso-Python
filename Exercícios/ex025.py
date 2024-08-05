print('\033[1;31;40m~= TAL DO ERA SÓ MAIS UM SILVA =~\033[m\n' + '\033[1;31m-\033[m' * 33)
nome = str(input('\033[1;31m•\033[m Digite seu nome completo: \n\033[1;31m-----> \033[m')).upper()
c = 'SILVA' in nome
print('\033[1;31m-\033[m' * 33)
if c is True:
    print('\033[1;32mSeu nome possuí "\033[4mSILVA\033[m\033[1;32m"!')
else:
    print('\033[1;31mSeu nome não possuí "\033[4mSILVA\033[m\033[1;31m"!')
