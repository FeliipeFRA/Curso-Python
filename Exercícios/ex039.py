from datetime import date
print('\033[1;32;40m    ~= TAL DO ALISTA =~    \033[m\n' + '\033[1;32m-\033[m' * 27)
print('SAIBA SE É A HORA DE SE \033[1;32mALISTAR\033[m AO \033[1;32mEXER\033[1;33mCÍT\033[1;34mO '
      'BRA\033[1;33mSIL\033[1;32mEIRO!\033[m')
sexo = str(input('\033[1;32m•\033[m Qual seu sexo:\n\033[1;32m[F] - FEMININO\n[M] - MASCULINO\n-----> '
                 '\033[m')).strip().upper()
ano = date.today().year
mes = date.today().month
if sexo == "F":
    print('Você \033[1;32mNÃO\033[m é obrigada a se \033[1;32mALISTAR\033[m!')
elif sexo == "M":
    anon = int(input('\033[1;32m•\033[m Ano de nascimento:\n\033[1;32m-----> \033[m'))
    idade = (ano - anon)
    print('\033[1;32m-\033[m' * 27)
    if idade == 18:
        print('Você \033[1;32mDEVE\033[m se alistar \033[1;32mESSE ANO\033[m!')
    elif 18 > idade > 0:
        if idade - 18 == -1:
            print('Você \033[1;32mDEVE\033[m se alistar daqui a \033[1;32m1 ANO\033[m!')
            print(f'Seu \033[1;32mALISTAMENTO\033[m será em \033[1;32m{ano + 1}\033[m!')
        else:
            print(f'Você \033[1;32mDEVE\033[m se alistar daqui a \033[1;32m{-idade + 18} ANOS\033[m!')
            print(f'Seu \033[1;32mALISTAMENTO\033[m será em \033[1;32m{ano + (-idade + 18)}\033[m!')
    elif 100 > idade > 18:
        if idade - 18 == 1:
            print('Você \033[1;31mDEVERIA\033[m ter se alistado a \033[1;31m1 ANO\033[m!')
            print(f'O ano do seu \033[1;31mALISTAMENTO\033[m foi em \033[1;31m{ano - 1}\033[m!')
        else:
            print(f'Você \033[1;31mDEVERIA\033[m ter se alistado a \033[1;31m{idade - 18} ANOS\033[m!')
            print(f'O ano do seu \033[1;31mALISTAMENTO\033[m foi em \033[1;31m{ano - (idade - 18)}\033[m!')
    else:
        print('\033[1;31mIDADE INVÁLIDA!\033[m Aperte \033[1;32mF6\033[m para \033[1;32mTENTAR NOVAMENTE!\033[m')
else:
    print('\033[1;31mSEXO INVÁLIDO!\033[m Aperte \033[1;32mF6\033[m para \033[1;32mTENTAR NOVAMENTE!\033[m')
