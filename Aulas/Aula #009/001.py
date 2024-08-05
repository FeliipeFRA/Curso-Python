num = input('num: ')
numdiv = list(num)
print(numdiv)
print(len(num))
if len(num) == 4:
    print(f'''
    Unidade: {num[3]}
    Dezena: {num[2]}
    Centena: {num[1]}
    Milhar: {num[0]}''')
elif len(num) == 3:
    print(f'''
        Unidade: {num[2]}
        Dezena: {num[1]}
        Centena: {num[0]}''')
else:
    print('pinto')