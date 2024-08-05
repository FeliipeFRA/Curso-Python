from random import randint
from time import sleep
print('\033[1;31;40m  ~= TAL DO ADVINHADOR =~  \033[m\n' + '\033[1;31m-\033[m' * 27)
num = randint(0, 5)
print('\033[1mOlá! Tenho um desafio para você!')
print('Pensei em um número...')
print('Entre 0 e 5...')
print('\033[1;31mDesafio VOCÊ a ADIVINHÁ-LO!!!\033[m\n' + '\033[1;31m-\033[m' * 27)
c = int(input('\n\033[1;31m•\033[m NÚMERO ESCOLHIDO: \n\033[1;31m-----> \033[m'))
print('\n\033[1;31mPROCESSANDO...\033[m\n')
sleep(2)
if c < 5:
    if c == num:
        print('\033[1;32mParabéns... Você acertou! >:P\033[m')
    else:
        print(f'\033[1;31mHAHAHA! Você ERROU! O número que eu pensei foi o {num}! XD\033[m')
else:
    print('\033[1;31mEi! O número escolhido não é válido! >:(\033[m')
