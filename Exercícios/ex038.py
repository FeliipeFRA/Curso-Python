print('\033[1;31;40m    ~= TAL DO COMPARA =~    \033[m\n' + '\033[1;31m-\033[m' * 28)
num1 = int(input('\033[1;31m• Valor 1:\n\033[1;31m----->\033[m '))
num2 = int(input('\033[1;32m• Valor 2:\n\033[1;32m----->\033[m '))
print('\033[1;31m-\033[m' * 28)
if num1 > num2:
    print(f'\033[1mO \033[1;31mVALOR 1 ({num1})\033[m\033[1m é \033[1;34mMAIOR\033[m que o \033[1;32mVALOR 2 ({num2})\033[m')
elif num2 > num1:
    print(f'\033[1mO \033[1;32mVALOR 2 ({num2})\033[m\033[1m é \033[1;34mMAIOR\033[m que o \033[1;31mVALOR 1 ({num1})\033[m')
else:
    print('\033[1mNão existe valor maior, ambos os valores são iguais')