def escreva(frase):
    print("\033[1;31m~" * (len(frase) + 4))
    print(f"{frase}".center((len(frase) + 4), " "))
    print("\033[1;31m~" * (len(frase) + 4))


# main
f = str(input("- Digite sua frase título: "))
escreva(f)