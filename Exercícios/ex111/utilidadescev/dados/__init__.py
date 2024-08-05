def leiaDinheiro(frase=""):
    # loop infinito ate que chegue a um return
    while True:
        v = input(f"{frase}").replace(",", ".").strip()
        # tenta retornar a conversão de v para float
        try:
            return float(v)
        # caso a conversão der errado:
        except ValueError:
            print(f"\033[1;31mO valor '{v}' é inválido! Tente novamente.\033[m")
