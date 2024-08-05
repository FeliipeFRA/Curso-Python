valores = []
maior = menor = 0
for v in range(0, 5):
    valores.append(int(input(f"- Valor na posição {v}: ")))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print("="*35)
print(f"- Você digitou os valores: \033[1;31m{valores}\033[m")
print(f"- O maior valor foi '{maior}', na posição: ", end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f"{c}...", end=' ')
print(f"\n- O menor valor foi '{menor}', na posição: ", end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f"{c}...", end=' ')
print()
