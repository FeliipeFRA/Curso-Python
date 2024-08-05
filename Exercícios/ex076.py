produtos = ('Farinha', 6,
            'Bife', 40,
            'Molho de Tomate', 3,
            'Arroz', 15,
            'Maionese', 9.75,
            'Coca-Cola', 8.50)
print(f"=" * 36)
print(f"~= TABELA DE PREÇOS =~".center(36, " "))
print(f"=" * 36)
for i in range(0, len(produtos), +2):
    print(f"{produtos[i]}".ljust(25, '.')+"R$", end="")
    print(f"{produtos[i+1]:.2f}".rjust(8, ' '), end="\n")
print(f"=" * 36)