from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print("=-" * 20)
    print(f"- Contagem de {inicio} até {fim} de {passo} em {passo}:")
    if inicio < fim:
        for i in range(inicio, fim+1, passo):
            print(f"\033[1;31m{i}", end=' ')
            sleep(1 / 3)
        print("FIM!\033[m")
    else:
        for i in range(inicio, fim-1, -passo):
            print(f"\033[1;31m{i}", end=' ')
            sleep(1 / 3)
        print("FIM!\033[m")


# main
contador(1, 10, 1)
contador(10, 0, -2)
print('=-' * 20)
print("- Crie sua contagem:")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i, f, p)