print('~= EXERCÍCIO 23 =~')
print('TAL DOS DÍGITOS')
num = int(input('Digite um número entre 0 e 9999: '))
m = num//1000
c = (num-m*1000)//100
d = (((num-(m*1000))-(c*100))//10)
u = (num-(m*1000)-(c*100)-(d*10)//1)
print(f'Unidade: {u:.0f}')
print(f'Dezena: {d:.0f}')
print(f'Centena: {c:.0f}')
print(f'Milhar: {m}')