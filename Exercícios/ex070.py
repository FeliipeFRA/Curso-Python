print("\033[1;33;40m   -= AMARELINHA SUPERMERCADOS =-   \033[m")
print("\033[1;33m-\033[m" * 36)
q = tot = overt = cheap = 0
cheaper = " "
while True:
    q += 1
    print(f"\033[1;33mITEM {q}\033[m")
    item = str(input("\033[1;33m-\033[m Nome do Produto: "))
    price = float(input("\033[1;33m-\033[m Preço do Produto: R$"))
    if q == 1 or price < cheap:
        cheap = price
        cheaper = item
    tot += price
    if price > 1000:
        overt += 1
    cont = str(input("\033[1;33m- Deseja adicionar mais um item ao carrinho? [S/N] \033[m")).strip().upper()
    while cont != ("S", "N"):
        print("\033[1;31mOpção inválida! Tente novamente.\033[m")
        cont = str(input("\033[1;33m- Deseja adicionar mais um item ao carrinho? [S/N] \033[m")).strip().upper()
    if cont == "N":
        break
print("\033[1;33m-\033[m" * 36)
print(f"\033[1;33;40m              NOTINHA:              \033[m")
print(f"\033[1;33m-\033[m Total de Itens: \033[1;33m{q}\033[m")
print(f"\033[1;33m-\033[m Valor da compra: \033[1;33mR${tot:.2f}\033[m")
print(f"\033[1;33m-\033[m Quantidade de itens acima de R$1000,00: \033[1;33m{overt}\033[m")
print(f"\033[1;33m-\033[m Item mais barato: \033[1;33m{cheaper.title()} [R${cheap:.2f}]\033[m")
