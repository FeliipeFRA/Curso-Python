from random import randint
from time import sleep
print("\033[1;31m=" * 35)
print("GERADOR DE JOGOS MEGASENA".center(35, " "))
print("=" * 35)
num = int(input("-\033[m Quantos palpites você quer gerar? \033[1;31m"))
print(f" GERANDO {num} JOGOS ".center(35, "="))
palpites = []
jogo = []
for p in range(0, num):
    while len(jogo) != 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
    palpites.append(jogo[:])
    jogo.clear()
for p in range(0, len(palpites)):
    sleep(1 / 2)
    print(f"{sorted(palpites[p])}".center(35, " "))
print(f" BOA SORTE MEU FI! ".center(35, "="))