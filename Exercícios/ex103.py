def ficha(n, g):
    if n == "":
        n = "desconhecido"
    if not g.isnumeric():
        g = "0"
    return f"O jogador {n} fez {g} gols."


nome = str(input("Nome do cabra: "))
gols = str(input("Gols marcados pelo cabra: "))
print(ficha(nome, gols))
