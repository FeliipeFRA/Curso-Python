end = False
num = tot = cont = 0
while not end:
    num = int(input("Número: "))
    if num == 999:
        end = True
        print(f"Quantidade: {cont}\nSoma: {tot}")
    else:
        tot += num
        cont += 1
