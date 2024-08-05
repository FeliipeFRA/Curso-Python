print('\033[1;31;40m    ~= TAL DA SOMA DOS MULTÍPLOS =~    \033[m\n' + '\033[1;31m-\033[m' * 39)
soma = 0
cont = 0
for i in range(1, 501):
    if i % 2 != 0:
        if i % 3 == 0:
            cont += 1
            soma += i
print(f'A soma dos {cont} valores, resulta em: {soma}')
