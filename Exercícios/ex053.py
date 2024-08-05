print('\033[1;31;40m ~= É O TAL DO PALÍNDROMO? =~ \033[m\n' + '\033[1;31m-\033[m' * 30)
frase = str(input('\033[1;31m-\033[m \033[1mFrase:\033[m\n\033[1;31m-----> \033[m')).strip()
frasej = ''.join(frase.upper().split())
'''for i in range(0, (len(frasej))):
    print(f'{frasej[i]}')'''
print('\033[1;31m-\033[m' * 30)
frasein = ""
for i in range(((len(frasej)) - 1), -1, -1):
    frasein += f'{frasej[i]}'
if frasej == frasein:
    print(f'\033[1;31m-\033[m A frase: \033[1;4;33m"{frase}"\033[m \033[1;32mÉ\033[m um \033[1;31mPALÍNDROMO!\033[m')
else:
    print(f'\033[1;31m-\033[m A frase: \033[1;4;33m"{frase}"\033[m \033[1;31mNÃO É\033[m um \033[1;31mPALÍNDROMO!'
          f'\033[m')
print('\033[1;31m-\033[m' * 30)
