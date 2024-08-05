from random import randint
print("\033[1;32;40m   ~= TAL DO ADIVINHADOR 2.0 =~    \033[m")
print("\033[1;32m-\033[m" * 35)
num = randint(0, 10)
win = False
tent = 0
print('\033[1;32m- Pensei em um número entre 0 e 10.\n- Tente advinhá-lo!                \033[m')
print("\033[1;32m-\033[m" * 35)
while not win:
    tent += 1
    c = int(input("- Seu palpite: "))
    if c < 0 or c > 10:
        print("Fora do intervalo! Tente novamente.")
    elif c == num:
        print("Acertou!")
        print("\033[1;32m-\033[m" * 35)
        print(f'\033[1;32m- Parabéns! Você acertou em {tent} tentativas. \033[m')
        win = True
    else:
        if c < num:
            print("Maior... Tente novamente!")
        else:
            print("Menor... Tente novamente!")
