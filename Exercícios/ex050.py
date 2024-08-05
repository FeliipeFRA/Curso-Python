print('\033[1;31;40m ~= TAL DA SOMA SÓ DE PARES =~ \033[m\n' + '\033[1;31m-\033[m' * 31)
total = 0
for i in range(1, 7):
    v = int(input(f'\033[1;31m-\033[m Valor {i}: '))
    if v % 2 == 0:
        total += v
print(f'Total: {total}')
