while True:
    tab = int(input("- Deseja ver a tabuada de qual número? "))
    if tab < 0:
        break
    print("-" * 25)
    for i in range (1, 11):
        print(f"{tab} x {i} = {tab * i}")
    print("-" * 25)
print("-" * 25)
print("Finalizando sistema...")