from random import randint
from time import sleep
x = int
print('\033[1;31;40m    ~= JOKENPÔ =~    \033[m\n' + '\033[1;31m-\033[m' * 21)
player = int(input("""Escolha:
\033[1;31m[1] -\033[m PEDRA
\033[1;31m[2] -\033[m PAPEL
\033[1;31m[3] -\033[m TESOURA
\033[1;31m-----> \033[m"""))
print('\033[1;31m-\033[m' * 21)
if player == 1 or player == 2 or player == 3:
    print('\033[1;31mJO...\033[m')
    sleep(1)
    print('\033[1;31mKEN...\033[m')
    sleep(1)
    print('\033[1;31mPÔ!\033[m')
    print('\033[1;31m-\033[m' * 21)
    pc = randint(1, 3)
    jog = "Nada"
    jogpc = "Nada"
    if player == 1:
        jog = "Pedra"
    elif player == 2:
        jog = "Papel"
    elif player == 3:
        jog = "Tesoura"
    if pc == 1:
        jogpc = 'Pedra'
    elif pc == 2:
        jogpc = 'Papel'
    elif pc == 3:
        jogpc = 'Tesoura'

    print(f'Jogador jogou {jog} e a máquina jogou {jogpc}')

    if player == pc:
        print('Empate')
    elif player == 1 and pc == 2:
        print('PC GANHOU')
    elif player == 1 and pc == 3:
        print('JOGADOR GANHOU')
    elif player == 2 and pc == 1:
        print('PC GANHOU')
    elif player == 1 and pc == 3:
        print('JOGADOR GANHOU')
else:
    print('\033[1mJogada \033[1;31mINVÁLIDA\033[m\033[1m! Tente novamente.\033[m')
