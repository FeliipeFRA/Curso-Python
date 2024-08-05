valores = []
for v in range(0, 5):
    n = int(input(f"- Insira um valor: "))
    if v == 0 or n >= valores[-1]:
        valores.append(n)
        print("Adicionado ao final da lista")
    else:
        for p in range(len(valores)):
            if n < valores[p]:
                valores.insert(p, n)
                print(f"Adicionado a {p}ª posição da lista")
                break
print(valores)
