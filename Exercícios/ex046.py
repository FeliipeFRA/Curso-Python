import emoji
from time import sleep
print('\033[1;31;40m    ~= SPACE TODAY =~    \033[m\n' + '\033[1;31m-\033[m' * 25)
start = str(input('''\033[1;31m- SACANI:\033[m Pressione \033[1;31m[ENTER]\033[m 
para iniciarmos o lançamento!\033[m'''))
print('\033[1;31m-\033[m' * 25)
for c in range(10, 0, -1):
    if c > 3:
        print(f'\033[1m{c}\033[m')
    else:
        print(f'\033[1;31m{c}\033[m')
    sleep(1)
print(emoji.emojize('            🌕'))
print('\n\n')
print(emoji.emojize('  🚀'))
print(emoji.emojize('🌏'))
print('\033[1;31m- SACANI:\033[m Decolou amigos da \033[1;31mASTRONOMIA!\033[m')