print('\033[1;31;40m    ~= TAL DA VIAGEM FILHO =~    \033[m\n' + '\033[1;31m-\033[m' * 33)
d = int(input("\033[1;31m•\033[m DISTÂNCIA DA VIAGEM \033[1;31m(Km's)\033[m: \n\033[1;31m-----> \033[m"))
print('\033[m' + '\033[1;31m-\033[m' * 33)
if d <= 200:
    print(f'A passagem para essa viagem custa: \033[1;4;33mR${(d * 0.5):.2f}\033[m')
else:
    print(f'A passagem para essa viagem custa: \033[1;4;33mR${(d * 0.45):.2f}\033[m')
