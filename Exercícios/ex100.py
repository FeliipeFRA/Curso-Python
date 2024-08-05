from time import sleep
from random import randint
num = []


def sorteia(lista):
    for i in range(0, 5):
        lista.append(randint(1, 10))
    print("Numeros sorteados: ", end='')
    for n in num:
        sleep(1 / 3)
        print(f"\033[1;31m{n} ", end='')


def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f"\033[m\nSoma dos valores pares: \033[1;31m{soma}\033[m")


# main
sorteia(num)
somapar(num)
sorteia(num)
somapar(num)