def leiaint(inp):
    valor = 0
    while True:
        n = str(input(f"{inp}"))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print("\033[1;31mERRO! Digite um número inteiro válido. \033[m")
    return valor


# main
n = leiaint("Digite um número: ")
print(f"Você inseriu o valor {n}")
