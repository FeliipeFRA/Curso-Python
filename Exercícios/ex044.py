print('\033[1;31;40m    ~= TAL DO PAGAMENTO =~    \033[m\n' + '\033[1;31m-\033[m' * 30)
p = float(input('\033[1;31m•\033[m Preço do produto:\033[1;31m\n-----> R$ \033[m'))
print('\033[1;31m-\033[m' * 30)
print('\033[1;31mFORMAS DE PAGAMENTO\033[m')
print('\033[1;31m[1] - \033[m\033[1mA vista no \033[1;31mDINHEIRO\033[m ou \033[1;31mPIX\033[m\033[m '
      '\033[1;31m(10% DE DESCONTO!)\033[m')
print('\033[1;31m[2] - \033[m\033[1mA vista no \033[1;31mCARTÃO\033[m \033[1;31m(5% DE DESCONTO)\033[m')
print('\033[1;31m[3] - \033[m\033[1mEm \033[1;31m2x\033[m no \033[1;31mCARTÃO\033[m \033[1;31m(PREÇO NORMAL)\033[m')
print('\033[1;31m[4] - \033[m\033[1mEm \033[1;31m3x ou mais\033[m no \033[1;31mCARTÃO\033[m '
      '\033[1;31m(20% DE JUROS)\033[m')
print('\033[1;31m-\033[m' * 30)
forma = int(input('\033[1;31m•\033[m Forma de pagamento \033[1;31m(1, 2, 3 ou 4)\033[m:\033[1;31m\n-----> \033[m'))
print('\033[1;31m-\033[m' * 30)
if forma == 1:
    print(f'\033[1;31m•\033[m \033[1mPREÇO TOTAL DO PRODUTO:\033[m\n\033[1;31mR${p - p * 0.10:.2f}\033[m')
elif forma == 2:
    print(f'\033[1;31m•\033[m \033[1mPREÇO TOTAL DO PRODUTO:\033[m\n\033[1;31mR${p - p * 0.05:.2f}\033[m')
elif forma == 3:
    print(f'\033[1mSua compra será parcelada em \033[1;31m2x\033[m de:\033[m\n\033[1;31mR${p/2:.2f}\033[m')
    print(f'\033[1;31m•\033[m \033[1mPREÇO TOTAL DO PRODUTO:\033[m\n\033[1;31mR${p:.2f}\033[m')
elif forma == 4:
    vezes = int(input('\033[1;31m•\033[m Será dividido em quantas vezes?\033[m\033[1;31m\n-----> \033[m'))
    if 2 < vezes:
        print(f'\033[1mSua compra será parcelada em \033[1;31m{vezes}x\033[m de:\033[m\n\033[1;31mR$'
              f'{(p + p * 0.2) / vezes:.2f}\033[m')
        print(f'\033[1;31m•\033[m \033[1mPREÇO TOTAL DO PRODUTO:\033[m\n\033[1;31m{p + p * 0.2:.2f}\033[m')
    else:
        print('\033[1mOpção de parcelamento \033[1;31mINVÁLIDA\033[m\033[1m! Tente novamente.\033[m')
else:
    print('\033[1mForma de pagamento \033[1;31mINVÁLIDA\033[m\033[1m! Tente novamente.\033[m')
