print('\033[1;31;40m~= TAL DO QUANDO A ESMOLA É DEMAIS O SANTO DESCONFIA =~\033[m\n' + '\033[1;31m-\033[m' * 55)
cidade = str(input('\033[1;31m•\033[m Em qual cidade você nasceu? \n\033[1;31m-----> \033[m')).strip()
cm = cidade.upper()
cs = cm.split()
print('\033[1;31m-\033[m' * 55)
if cs[0] == 'SANTO':
    print('\033[1;32mO nome da sua cidade começa com "\033[4mSANTO\033[m\033[1;32m"!')
else:
    print('\033[1;31mO nome da sua cidade não começa com "\033[4mSANTO\033[m\033[1;31m"!')
