print('\033[1;31;40m    ~= TAL DA MULTA FILHO =~    \033[m\n' + '\033[1;31m-\033[m' * 32)
v = float(input('\033[1;31m•\033[m VELOCIDADE DO VEÍCULO \033[1;31m(Km/h)\033[m: \n\033[1;31m-----> \033[m'))
print('\033[m' + '\033[1;31m-\033[m' * 32)
if v > 80:
    print('\033[1;31mO veículo foi multado! Muito rápido fiho!\033[m')
    print(f'\033[1mValor da multa:\033[m \033[1;4;33mR${((v-80)*7):.2f}\033[m')
elif v < 40:
    print('\033[1;31mO veículo foi multado! Muito lento filho!\033[m')
    print(f'\033[1mValor da multa:\033[m \033[1;4;33mR${(((v - 40) * -1) * 7):.2f}\033[m')
else:
    print('\033[1;32mO veículo está dentro do limite permitido. Boa cria!\033[m')
