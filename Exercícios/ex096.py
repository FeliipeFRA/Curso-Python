def area(larg, comp):
    print("=" * 50)
    print(f"- A área do seu terreno de \033[1;31m{larg} X {comp}\033[m é de: "
          f"\033[1;31m{larg * comp}m²\033[m")


# main
l = float(input("- Largura do seu terreno (m): "))
c = float(input("- Comprimento do seu terreno (m): "))
area(l, c)
