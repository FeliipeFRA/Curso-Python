from datetime import date
atual = date.today().year

print('\033[1;34;40m      ~= TAL DAS IDADES =~      \033[m\n' + '\033[1;34m-\033[m' * 32)
print('\033[1;34mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
nasc = int(input('\033[1;34m•\033[m\033[1m Insira seu ano de nascimento para saber sua categoria:\033[m\n'
                 '\033[1;34m-----> \033[m'))
idade = atual - nasc
print('\033[1;34m-\033[m' * 32)
print(f'\033[1;34m•\033[m\033[1m Você possui \033[1;34m{idade} ANOS!\033[m')
if 0 < idade < 9:
    print('\033[1mSua \033[1;34mCATEGORIA\033[m\033[1m é: \033[1;34mMIRIM\033[m')
elif idade < 14:
    print('\033[1mSua \033[1;34mCATEGORIA\033[m\033[1m é: \033[1;34mINFANTIL\033[m')
elif idade < 19:
    print('\033[1mSua \033[1;34mCATEGORIA\033[m\033[1m é: \033[1;34mJUNIOR\033[m')
elif idade < 25:
    print('\033[1mSua \033[1;34mCATEGORIA\033[m\033[1m é: \033[1;34mSÊNIOR\033[m')
elif idade < 100:
    print('\033[1mSua \033[1;34mCATEGORIA\033[m\033[1m é: \033[1;34mMASTER\033[m')
else:
    print('\033[1;31mIdade inválida! >:(\033[m')
