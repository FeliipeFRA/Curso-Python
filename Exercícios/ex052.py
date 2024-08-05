print('\033[1;31;40m ~= É PRIMO? =~ \033[m\n' + '\033[1;31m-\033[m' * 16)
num = int(input('\033[1;31m-\033[m \033[1mValor a ser verificado:\033[m\n\033[1;31m-----> \033[m'))
primo = True
for i in range(1, num+1):
    if i != 1 and i != num:
        if num % i == 0:
            primo = False
    elif num == 1:
        primo = False
print('\033[1;31m-\033[m' * 16)
if primo:
    print('\033[1;31m- É\033[m primo')
else:
    print('\033[1;31m- NÃO É\033[m primo')
