from random import randint
wins = 0
result = ""
op = ""
print("\033[1;40m    ~= JOGO DE \033[1;31mPAR\033[m\033[1;40m OU \033[1;32mÍMPAR\033[m\033[1;40m =~    \033[m")
while True:
    op = str(input("- Par \033[1;31m[P]\033[m ou Ímpar \033[1;32m[I]\033[m:\n-----> ")).strip().upper()[0]
    if op in ("P", "I"):
        num = int(input("- Qual número você deseja jogar? "))
        pc = randint(0, 10)
        tot = num + pc
        if tot % 2 == 0:
            result = "PAR"
        else:
            result = "ÍMPAR"
        print("-" * 34)
        if op == result[0]:
            print(f"- Você jogou {num} e eu joguei {pc}. Total de {tot} deu {result}")
            print("Você venceu! Vamos jogar novamente... :I")
            print("-" * 34)
            wins += 1
        else:
            print(f"- Você jogou {num} e eu joguei {pc}. Total de {tot} deu {result}")
            print("Você perdeu! XD")
            print("-" * 34)
            if wins == 0:
                print("SEU LIXO! NÃO ME VENCEU NENHUMA VEZ! XD")
            elif wins == 1:
                print("GAME OVER! Você só me venceu 1 vez só ;)")
            else:
                print(f"GAME OVER! Você venceu {wins} vezes!")
            break
    else:
        print("\033[1;31m- Opção inválida! Tente novamente.\033[m")
        print("-" * 34)
