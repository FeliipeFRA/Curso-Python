end = False
num = cont = tot = menor = maior = 0
while not end:
    num = int(input("Valor ---> "))
    if cont == 0:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont += 1
    tot += num
    endop = False
    while not endop:
        op = str(input("Deseja continuar? (S/N) ")).strip().upper()[0]
        if op in ("S"):
            print("-------------------------------------")
            endop = True
        elif op in ("N"):
            endop = True
            end = True
            print("-------------------------------------")
            print(f"- Quantidade de valores recebidos: {cont}")
            print(f"- Média dos valores recebidos: {tot / cont}")
            print(f"- Maior valor recebido: {maior}")
            print(f"- Menor valor recebido: {menor}")
        else:
            print("\033[1;31mOpção inválida!\033[m")