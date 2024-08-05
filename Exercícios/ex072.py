numeros = ("Zéro", "Un", "Deux", "Trois", "Quatre", "Cinq", "Six", "Sept", "Huit", "Neuf", "Dix", "Onze", "Douze",
           "Treize", "Quatorze", "Quinze", "Seize", "Dix-Sept", "Dix-Huit", "Dix-Neuf", "Vingt")
print("    ~= NÚMEROS EM FRANCÊS =~   ")
while True:
    while True:
        print("=" * 31)
        n = int(input("- Insira um número de 0 a 20: "))
        if 0 <= n <= 20:
            break
        print("\033[1;31mNúmero fora do intervalo! Tente novamente.\033[m")
    print("=" * 31)
    print(f"A escrita por extenso do número \033[1;31m{n}\033[m em \033[1;31mFrancês\033[m é: \033[1;31m{numeros[n]}\033[m")
    while True:
        cont = str(input("- Deseja continuar? [S/N] ")).strip().upper()[0]
        if cont not in ("S", "N"):
            print("\033[1;31mNúmero fora do intervalo! Tente novamente.\033[m")
        else:
            break
    if cont == "N":
        break
print(f"FIM!")