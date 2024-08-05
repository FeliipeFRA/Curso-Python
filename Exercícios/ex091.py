from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'P1': randint(1, 6), 'P2': randint(1, 6), 'P3': randint(1, 6), 'P4': randint(1, 6)}
print("APERTE \033[1;31m[ENTER]\033[m PARA INICIAR")
start = str(input("\033[1;31m=" * 30))
print("ROLANDO DADOS...\033[m")
print("\033[1;31m=" * 30)
for k, v in jogadores.items():
    print(f"\033[1;31m-\033[m {k} tirou {v}")
    sleep(1)
print("\033[1;31m=" * 30)
print(f"{'RANKING FINAL':^30}\033[m")
print("\033[1;31m=" * 30)
sleep(1)
ranking = dict(sorted(jogadores.items(), key=itemgetter(1), reverse=True))
print(f"{'POSIÇÃO'.center(10, ' ')}{'PLAYER'.center(10, ' ')}{'VALOR'.center(10, ' ')}")
r = 0
for k, v in ranking.items():
    r += 1
    print(f"\033[1;31m{r:^10}\033[m{k:^10}{v:^10}")