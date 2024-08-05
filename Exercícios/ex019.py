import random
print('\033[1;31;40m~= TAL DO SORTEIO =~\033[m\n' + '\033[1;31m-\033[m' * 20)
n1 = input('\033[1;31m•\033[m Aluno(a) \033[1;31m1\033[m: ')
n2 = input('\033[1;32m•\033[m Aluno(a) \033[1;32m2\033[m: ')
n3 = input('\033[1;33m•\033[m Aluno(a) \033[1;33m3\033[m: ')
n4 = input('\033[1;34m•\033[m Aluno(a) \033[1;34m4\033[m: ')
nomes = [n1, n2, n3, n4]
r = random.choice(nomes)
print('\033[1;31m-\033[m' * 20)
if r == n1:
    print(f'O(a) escolhido(a) para apagar a lousa foi: \033[1;31m{r}\033[m.')
elif r == n2:
    print(f'O(a) escolhido(a) para apagar a lousa foi: \033[1;32m{r}\033[m.')
elif r == n3:
    print(f'O(a) escolhido(a) para apagar a lousa foi: \033[1;33m{r}\033[m.')
elif r == n4:
    print(f'O(a) escolhido(a) para apagar a lousa foi: \033[1;34m{r}\033[m.')
