print('~= EXERCÍCIO 23 =~')
print('TAL DOS DÍGITOS')
num = int(input('Digite um número entre 0 e 9999: '))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print(f'Unidade: {u:.0f}')
print(f'Dezena: {d:.0f}')
print(f'Centena: {c:.0f}')
print(f'Milhar: {m}')
