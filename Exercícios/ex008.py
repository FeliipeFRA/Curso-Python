print('\033[1;31;40m~= CONVERSOR DE MEDIDAS =~\033[m\n' + '\033[1;31m-\033[m' * 26)
m = float(input('\033[1;31m•\033[m Insira uma medida em \033[1;31mMETROS\033[m:\n\033[1;31m-----> \033[m'))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'\033[1;31m•\033[m Sua medida em \033[1;32mQUILÔMETROS\033[m é: \033[1;4;32m{km}km\033[m.')
print(f'\033[1;31m•\033[m Sua medida em \033[1;33mHECTÔMETROS\033[m é: \033[1;4;33m{hm:}hm\033[m.')
print(f'\033[1;31m•\033[m Sua medida em \033[1;34mDECÂMETROS\033[m é: \033[1;4;34m{dam:}dam\033[m.')
print(f'\033[1;31m•\033[m Sua medida em \033[1;35mDECÍMETROS\033[m é: \033[1;4;35m{dm:.0f}dm\033[m.')
print(f'\033[1;31m•\033[m Sua medida em \033[1;36mCENTÍMETROS\033[m é: \033[1;4;36m{cm:.0f}cm\033[m.')
print(f'\033[1;31m•\033[m Sua medida em \033[1;37mMILÍMETROS\033[m é: \033[1;4;37m{mm:.0f}mm\033[m.')
