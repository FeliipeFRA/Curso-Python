print('\033[1;31;40m    ~= TAL DA MÉDIA =~    \033[m\n' + '\033[1;31m-\033[m' * 26)
n1 = float(input('\033[1;31m•\033[m Insira a nota do \033[1;31mPRIMEIRO BIMESTRE:\n-----> \033[m'))
n2 = float(input('\033[1;32m•\033[m Insira a nota do \033[1;32mSEGUNDO BIMESTRE:\n-----> \033[m'))
m = (n1 + n2) / 2
print('\033[1;31m-\033[m' * 26)
if (10 < n1 or n1 < 0) and (10 < n2 or n2 < 0):
    print('\033[1;31m• AMBAS AS NOTAS SÃO INVÁLIDAS, Aperte "F6" e tente novamente!\033[m')
elif 10 < n1 or n1 < 0:
    print('\033[1;31m•\033[m \033[1;31mNOTA 1\033[m inválida! Aperte "F6" e tente novamente!')
elif 10 < n2 or n2 < 0:
    print('\033[1;32m•\033[m \033[1;32mNOTA 2\033[m inválida! Aperte "F6" e tente novamente!')
else:
    print(f'Sua média foi \033[1;4m{m:.2f}\033[m')
    if m < 5:
        print('\033[1;31mINFELIZMENTE você foi REPROVADO! :(\033[m')
    elif 5 <= m < 7:
        print('\033[1;33mVocê está de recuperação, estude bastante e passe de ano!\033[m')
    else:
        print('\033[1;32mPARABÉNS! Você foi APROVADO! XD')
